from pydantic import BaseModel
from datetime import date
from decimal import Decimal

class DriverWeekDataCreate(BaseModel):
    driver_id: int
    scenario_id: int
    week_start_date: date
    mon_km: Decimal
    tue_km: Decimal
    wed_km: Decimal
    thu_km: Decimal
    fri_km: Decimal
    sat_km: Decimal
    sun_km: Decimal
    seatbelt_violations: int


class DriverWeekDataRead(BaseModel):
    driver_week_id: int
    week_start_date: date

    mon_km: Decimal
    tue_km: Decimal
    wed_km: Decimal
    thu_km: Decimal
    fri_km: Decimal
    sat_km: Decimal
    sun_km: Decimal

    seatbelt_violations: int

    driver_id: int
    driver_name: str

    scenario_id: int
    scenario_name: str