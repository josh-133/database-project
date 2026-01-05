from fastapi import FastAPI
from routers import dwd_routes, driver_routes, scenario_routes

app = FastAPI()

app.include_router(dwd_routes.router)
app.include_router(driver_routes.router)
app.include_router(scenario_routes.router)