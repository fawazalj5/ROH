from fastapi import FastAPI
from simulation.engine import SimulationEngine
from agents.base_agent import create_base_agent

app = FastAPI()

@app.post("/simulation")
def run_simulation_endpoint(epochs: int = 100, num_agents: int = 1):
    """
    Runs a simulation with the specified number of agents and epochs.
    """
    agents = [create_base_agent(f"agent_{i}") for i in range(num_agents)]
    engine = SimulationEngine(agents)
    engine.run_simulation(epochs)

    # For simplicity, we'll just return the final state of the first agent.
    final_state = engine.agents[0].omega_t.tolist()
    return {"final_state": final_state}
