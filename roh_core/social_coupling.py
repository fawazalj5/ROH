import numpy as np

def cooperative_coupling(agent1_omega_t, agent2_omega_t, strength):
    """
    A cooperative coupling model where agents move towards each other's state.
    """
    diff = agent2_omega_t - agent1_omega_t
    return agent1_omega_t + strength * diff, agent2_omega_t - strength * diff

def competitive_coupling(agent1_omega_t, agent2_omega_t, strength):
    """
    A competitive coupling model where agents move away from each other's state.
    """
    diff = agent2_omega_t - agent1_omega_t
    return agent1_omega_t - strength * diff, agent2_omega_t + strength * diff

def influence_coupling(influencer_omega_t, influenced_omega_t, strength):
    """
    An influence coupling model where one agent's state influences another.
    """
    diff = influencer_omega_t - influenced_omega_t
    return influencer_omega_t, influenced_omega_t + strength * diff
