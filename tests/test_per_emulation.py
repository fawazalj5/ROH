import unittest
import numpy as np
from roh_core.per_emulation import stochastic_fluctuation, entanglement_coupling

class TestPerEmulation(unittest.TestCase):

    def test_stochastic_fluctuation(self):
        omega_t = np.array([0.5, 0.5])
        fluctuated_omega = stochastic_fluctuation(omega_t, 0.1)
        self.assertNotEqual(np.sum(omega_t), np.sum(fluctuated_omega))

    def test_entanglement_coupling(self):
        agent1_omega_t = np.array([0.2, 0.8])
        agent2_omega_t = np.array([0.8, 0.2])
        coupled1, coupled2 = entanglement_coupling(agent1_omega_t, agent2_omega_t, 0.5)

        expected = np.array([0.5, 0.5])
        np.testing.assert_allclose(coupled1, expected)
        np.testing.assert_allclose(coupled2, expected)

if __name__ == '__main__':
    unittest.main()
