from fastapi import FastAPI
from app.api import category_endpoints
from app.database import engine
from app.models import category

category.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(category_endpoints.router, prefix="/api/v1")
