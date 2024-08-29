from fastapi import FastAPI
from .config import settings
from .routers import example

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

app.include_router(example.router)