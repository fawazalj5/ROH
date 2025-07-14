from fastapi import FastAPI
from .tasks import run_simulation_task

app = FastAPI()

@app.post("/simulation")
def run_simulation_endpoint(epochs: int = 100, num_agents: int = 1):
    """
    Triggers a simulation task to run in the background.
    """
    task = run_simulation_task.delay(epochs, num_agents)
    return {"task_id": task.id}

@app.get("/simulation/{task_id}")
def get_simulation_result(task_id: str):
    """
    Retrieves the result of a simulation task.
    """
    task = run_simulation_task.AsyncResult(task_id)
    if task.ready():
        return {"status": "SUCCESS", "result": task.result}
    else:
        return {"status": "PENDING"}
