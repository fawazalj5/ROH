import unittest
from simulation.engine import SimulationEngine
from agents.base_agent import create_base_agent

class TestIntegration(unittest.TestCase):

    def test_simulation_run(self):
        """
        Tests that a simulation can be created and run without errors.
        """
        try:
            agents = [create_base_agent("agent_0")]
            engine = SimulationEngine(agents)
            engine.run_simulation(10)
        except Exception as e:
            self.fail(f"Simulation run failed with exception: {e}")

if __name__ == '__main__':
    unittest.main()
