from fastapi import FastAPI
from app.config.database import Base, engine  
import os

from app.exceptions.handlers import load_exception_handlers 
from app.api.routes import load_routes 

app = FastAPI(title="My FastAPI App")



# Create tables
if os.getenv("APP_ENV") == "development":
    Base.metadata.create_all(bind=engine)
 

# Register routes
load_routes(app)


# Load exception handlers
load_exception_handlers(app)