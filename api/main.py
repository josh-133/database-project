from fastapi import FastAPI

app = FastAPI(
    title="Vehicle Scenario API",
    version="0.1.0",
    description="API layer for the SQL project"
)

@app.get("/")
def root():
    return {"status": "API running"}