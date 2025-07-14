import unittest
import numpy as np
from roh_core.social_coupling import cooperative_coupling, competitive_coupling, influence_coupling

class TestSocialCoupling(unittest.TestCase):

    def test_cooperative_coupling(self):
        agent1_omega_t = np.array([0.2, 0.8])
        agent2_omega_t = np.array([0.8, 0.2])
        coupled1, coupled2 = cooperative_coupling(agent1_omega_t, agent2_omega_t, 0.1)

        # The states should move closer to each other
        self.assertLess(np.linalg.norm(coupled1 - coupled2), np.linalg.norm(agent1_omega_t - agent2_omega_t))

    def test_competitive_coupling(self):
        agent1_omega_t = np.array([0.2, 0.8])
        agent2_omega_t = np.array([0.8, 0.2])
        coupled1, coupled2 = competitive_coupling(agent1_omega_t, agent2_omega_t, 0.1)

        # The states should move further apart
        self.assertGreater(np.linalg.norm(coupled1 - coupled2), np.linalg.norm(agent1_omega_t - agent2_omega_t))

    def test_influence_coupling(self):
        influencer = np.array([1.0, 1.0])
        influenced = np.array([0.0, 0.0])
        _, new_influenced = influence_coupling(influencer, influenced, 0.5)

        # The influenced agent should move towards the influencer
        self.assertAlmostEqual(np.sum(new_influenced), 1.0)

if __name__ == '__main__':
    unittest.main()
