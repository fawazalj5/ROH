import unittest
import numpy as np
from roh_core.operators import update_omega, calculate_chi, detect_epsilon_emergence

class TestOperators(unittest.TestCase):

    def test_update_omega(self):
        omega_t = np.array([0.5, 0.5])
        goal_state = np.array([1.0, 1.0])
        external_stimuli = np.array([0.1, 0.1])
        alpha, gamma, beta, delta = 0.8, 0.1, 0.2, 0.0

        omega_t_plus_1 = update_omega(omega_t, alpha, gamma, beta, delta, goal_state, external_stimuli)

        expected = (0.8 * omega_t) + (0.2 * (goal_state - omega_t)) + (0.1 * external_stimuli)
        np.testing.assert_allclose(omega_t_plus_1, expected, rtol=1e-6)

    def test_calculate_chi(self):
        # A constant state should have high coherence (chi -> 1)
        omega_t_high_coherence = np.array([0.5, 0.5, 0.5, 0.5])
        chi_high = calculate_chi(omega_t_high_coherence)
        self.assertAlmostEqual(chi_high, 1.0)

        # A noisy state should have low coherence
        omega_t_low_coherence = np.array([0.0, 1.0, 0.0, 1.0])
        chi_low = calculate_chi(omega_t_low_coherence)
        self.assertLess(chi_low, 0.8)

    def test_detect_epsilon_emergence(self):
        self.assertTrue(detect_epsilon_emergence(0.95, threshold=0.9))
        self.assertFalse(detect_epsilon_emergence(0.85, threshold=0.9))

if __name__ == '__main__':
    unittest.main()
