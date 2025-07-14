from roh_core.operators import update_omega, calculate_chi, detect_epsilon_emergence
from roh_core.models import PhenomenalField
from roh_core.per_emulation import stochastic_fluctuation
from roh_core.social_coupling import cooperative_coupling, competitive_coupling, influence_coupling

class SimulationEngine:
    def __init__(self, agents, initial_field=None, coupling_strength=0.1):
        self.agents = agents
        self.phenomenal_field = initial_field if initial_field else PhenomenalField()
        self.t = 0
        self.coupling_strength = coupling_strength

    def run_epoch(self, external_stimuli_map=None, social_coupling_model='cooperative'):
        """
        Runs a single epoch of the simulation.
        """
        if external_stimuli_map is None:
            external_stimuli_map = {}

        # First, update the state of each agent individually
        for agent in self.agents:
            # Get external stimuli for the agent, if any
            external_stimuli = external_stimuli_map.get(agent.id, 0)

            # Update the agent's state
            agent.omega_t = update_omega(
                agent.omega_t,
                agent.parameters['alpha'],
                agent.parameters['gamma'],
                agent.parameters['beta'],
                agent.parameters['delta'],
                agent.goal_state,
                external_stimuli
            )

        # Then, apply the selected social coupling model
        if len(self.agents) > 1:
            coupling_function = self.get_coupling_function(social_coupling_model)
            for i in range(len(self.agents)):
                for j in range(i + 1, len(self.agents)):
                    self.agents[i].omega_t, self.agents[j].omega_t = coupling_function(
                        self.agents[i].omega_t,
                        self.agents[j].omega_t,
                        self.coupling_strength
                    )

        # Finally, calculate coherence and record the state
        for agent in self.agents:
            # Calculate coherence and check for emergence
            agent.chi = calculate_chi(agent.omega_t)
            agent.epsilon_emergence = detect_epsilon_emergence(agent.chi)

            # Record the new state in the phenomenal field
            self.phenomenal_field.record_state(self.t, agent.id, agent.omega_t)

        self.t += 1

    def get_coupling_function(self, model_name):
        if model_name == 'cooperative':
            return cooperative_coupling
        elif model_name == 'competitive':
            return competitive_coupling
        elif model_name == 'influence':
            # For simplicity, we'll assume the first agent is the influencer
            return lambda agent1, agent2, strength: influence_coupling(agent1, agent2, strength)
        else:
            raise ValueError(f"Unknown social coupling model: {model_name}")

    def run_simulation(self, epochs, external_stimuli_map=None):
        """
        Runs the simulation for a given number of epochs.
        """
        for _ in range(epochs):
            self.run_epoch(external_stimuli_map)
