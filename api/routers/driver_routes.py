from fastapi import APIRouter
from db.driver_queries import (
    get_drivers,
    create_driver,
    update_driver,
    delete_driver,
)
from schemas.driver_schema import (
    DriverCreate,
    DriverRead,
    DriverUpdate,
)

router = APIRouter(prefix="/driver", tags=["Driver"])

@router.get("/", response_model=list[DriverRead])
def read_all():
    return get_drivers()


@router.post("/", status_code=201)
def create(data: DriverCreate):
    new_id = create_driver(data)
    return {"driver_id": new_id}

@router.put("/")
def update(driver_id: int, data: DriverUpdate):
    return update_driver(driver_id, data)

@router.delete("/")
def delete(driver_id: int):
    return delete_driver(driver_id)