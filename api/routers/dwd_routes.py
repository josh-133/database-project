from fastapi import APIRouter, HTTPException
from db.driver_week_data import (
    get_driver_week_data,
    create_driver_week_data
)
from schemas.driver_week_data import (
    DriverWeekDataCreate,
    DriverWeekDataRead
)

router = APIRouter(prefix="/driver-week-data", tags=["Driver Week Data"])

@router.get("/", response_model=list[DriverWeekDataRead])
def read_all():
    return get_driver_week_data()


@router.post("/", status_code=201)
def create(data: DriverWeekDataCreate):
    new_id = create_driver_week_data(data)
    return {"driver_week_id": new_id}