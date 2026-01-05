from pydantic import BaseModel
from datetime import datetime

class ScenarioCreate(BaseModel):
    scenario_name: str
    scenario_description: str
    predicted_weather: str
    start_time: datetime


class ScenarioRead(BaseModel):
    scenario_id: int
    scenario_name: str
    scenario_description: str
    predicted_weather: str
    start_time: datetime

    
class ScenarioUpdate(BaseModel):
    scenario_id: int
    scenario_name: str
    scenario_description: str
    predicted_weather: str
    start_time: datetime