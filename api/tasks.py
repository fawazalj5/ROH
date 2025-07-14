from celery import Celery
from simulation.engine import SimulationEngine
from agents.base_agent import create_base_agent

celery_app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@celery_app.task
def run_simulation_task(epochs: int, num_agents: int):
    """
    Celery task to run a simulation asynchronously.
    """
    agents = [create_base_agent(f"agent_{i}") for i in range(num_agents)]
    engine = SimulationEngine(agents)
    engine.run_simulation(epochs)

    # For simplicity, we'll just return the final state of the first agent.
    final_state = engine.agents[0].omega_t.tolist()
    return {"final_state": final_state}
