from fastapi import FastAPI
from app.controller import router as task_router

app = FastAPI()

app.include_router(task_router)