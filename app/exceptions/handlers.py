from fastapi import Request
from fastapi.responses import JSONResponse
from jose import JWTError
from starlette.status import HTTP_401_UNAUTHORIZED
from fastapi.exceptions import RequestValidationError 
from starlette.exceptions import HTTPException as StarletteHTTPException
from slowapi import _rate_limit_exceeded_handler 
from slowapi.errors import RateLimitExceeded
# Custom handler for JWT errors
async def jwt_exception_handler(request: Request, exc: JWTError):
    return JSONResponse(
        status_code=HTTP_401_UNAUTHORIZED,
        content={"detail": "Invalid or expired token"},
    )


async def validation_exception_handler(request, exc):
    return JSONResponse(status_code=422, content={"detail": "Invalid input"})

async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


def load_exception_handlers(app): 
    app.add_exception_handler(JWTError, jwt_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
# (Optional) Add more custom handlers here for different exceptions
