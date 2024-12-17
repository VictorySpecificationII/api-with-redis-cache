# app/main.py
from fastapi import FastAPI
from app.endpoints import router as basic_router
from app.db_endpoints import router as db_router

app = FastAPI()

# Include routers
app.include_router(basic_router)
app.include_router(db_router)
