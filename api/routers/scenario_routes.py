from fastapi import APIRouter
from db.scenario_queries import (
    get_scenarios,
    create_scenario,
    update_scenario,
    delete_scenario,
)
from schemas.scenario_schema import (
    ScenarioCreate,
    ScenarioRead,
    ScenarioUpdate,
)

router = APIRouter(prefix="/scenario", tags=["Scenario"])

@router.get("/", response_model=list[ScenarioRead])
def read_all():
    return get_scenarios()


@router.post("/", status_code=201)
def create(data: ScenarioCreate):
    new_id = create_scenario(data)
    return {"scenario_id": new_id}

@router.put("/")
def update(scenario_id: int, data: ScenarioUpdate):
    return update_scenario(scenario_id, data)

@router.delete("/")
def delete(scenario_id: int):
    return delete_scenario(scenario_id)