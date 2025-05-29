from fastapi import FastAPI
from app.config.database import Base, engine
from app.api.v1 import user as user_routes

app = FastAPI(title="My FastAPI App")

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(user_routes.router, prefix="/api/v1/users", tags=["Users"])
