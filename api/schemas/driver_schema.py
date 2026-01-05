from pydantic import BaseModel
from datetime import date

class DriverCreate(BaseModel):
    driver_name: str
    employee_number: str
    employee_start_date: date


class DriverRead(BaseModel):
    driver_id: int
    driver_name: str
    employee_number: str
    employee_start_date: date

    
class DriverUpdate(BaseModel):
    driver_id: int
    driver_name: str
    employee_number: str
    employee_start_date: date