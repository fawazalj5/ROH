import numpy as np

class NoeticAgent:
    def __init__(self, agent_id, initial_state, parameters):
        self.id = agent_id
        self.omega_t = np.array(initial_state, dtype=np.float32)
        self.parameters = parameters
        self.chi = 0.0
        self.epsilon_emergence = False
        self.per_active = False
        self.goal_state = np.zeros_like(self.omega_t)
        self.memory_graph = None  # To be implemented

class PhenomenalField:
    def __init__(self):
        self.field_data = {}  # Using a dict for sparse representation for now

    def record_state(self, t, agent_id, omega_t):
        if t not in self.field_data:
            self.field_data[t] = {}
        self.field_data[t][agent_id] = omega_t.copy()

    def get_state(self, t, agent_id):
        return self.field_data.get(t, {}).get(agent_id)
