from fastapi import APIRouter
from db.dwd_queries import (
    get_driver_week_data,
    create_driver_week_data,
    update_driver_week_data,
    delete_driver_week_data,
)
from schemas.dwd_schema import (
    DriverWeekDataCreate,
    DriverWeekDataRead,
    DriverWeekDataUpdate,
)

router = APIRouter(prefix="/driver-week-data", tags=["Driver Week Data"])

@router.get("/", response_model=list[DriverWeekDataRead])
def read_all():
    return get_driver_week_data()


@router.post("/", status_code=201)
def create(data: DriverWeekDataCreate):
    new_id = create_driver_week_data(data)
    return {"driver_week_id": new_id}

@router.put("/")
def update(driver_week_id: int, data: DriverWeekDataUpdate):
    return update_driver_week_data(driver_week_id, data)

@router.delete("/")
def delete(driver_week_id: int):
    return delete_driver_week_data(driver_week_id)