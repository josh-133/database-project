from fastapi import FastAPI
from routers import dwd_routes

app = FastAPI()

app.include_router(dwd_routes.router)