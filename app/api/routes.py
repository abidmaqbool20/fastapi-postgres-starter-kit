from slowapi import Limiter
from slowapi.util import get_remote_address 

from app.api.v1 import user as user_routes
from app.api.v1 import auth as auth_routes
from app.api.v1 import role as role_routes
from app.api.v1 import engine_request as engine_request_routes





# Include routers
def load_routes(app):  
    app.include_router(auth_routes.router, prefix="/api/v1/auth", tags=["Auth"])
    app.include_router(user_routes.router, prefix="/api/v1/users", tags=["Users"])
    app.include_router(role_routes.router, prefix="/api/v1/roles", tags=["Roles"])
    app.include_router(engine_request_routes.router, prefix="/api/v1/engine-request", tags=["EngineRequest"])


# Configure Rate Limiter
def add_rate_limiter(app):
    limiter = Limiter(key_func=get_remote_address)
    app.state.limiter = limiter
