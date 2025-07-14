from roh_core.models import NoeticAgent

def create_base_agent(agent_id, state_size=10):
    """
    Creates a basic Noetic Agent with default parameters.
    """
    initial_state = [0.0] * state_size
    parameters = {
        "alpha": 0.8,
        "gamma": 0.1,
        "beta": 0.2,
        "delta": 0.05
    }
    return NoeticAgent(agent_id, initial_state, parameters)
