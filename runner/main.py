import argparse
from simulation.engine import SimulationEngine
from agents.base_agent import create_base_agent
from visualizer.main import visualize_field

def main():
    parser = argparse.ArgumentParser(description="ROH Simulation Platform")
    parser.add_argument("--epochs", type=int, default=100, help="Number of epochs to run the simulation for.")
    parser.add_argument("--num-agents", type=int, default=1, help="Number of agents to include in the simulation.")
    parser.add_argument("--visualize", action="store_true", help="Visualize the phenomenal field of the first agent.")

    args = parser.parse_args()

    # Create agents
    agents = [create_base_agent(f"agent_{i}") for i in range(args.num_agents)]

    # Create and run the simulation engine
    engine = SimulationEngine(agents)
    engine.run_simulation(args.epochs)

    print("Simulation finished.")
    print(f"Final state of agent_0: {engine.agents[0].omega_t}")

    # Visualize the results if requested
    if args.visualize:
        if args.num_agents > 0:
            visualize_field(engine.phenomenal_field, "agent_0")
        else:
            print("No agents to visualize.")

if __name__ == "__main__":
    main()
