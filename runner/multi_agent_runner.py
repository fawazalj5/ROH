import argparse
from simulation.engine import SimulationEngine
from agents.base_agent import create_base_agent
from visualizer.main import visualize_field

def main():
    parser = argparse.ArgumentParser(description="ROH Multi-Agent Simulation Runner")
    parser.add_argument("--epochs", type=int, default=100, help="Number of epochs to run the simulation for.")
    parser.add_argument("--num-agents", type=int, default=2, help="Number of agents to include in the simulation.")
    parser.add_argument("--coupling-model", type=str, default="cooperative", choices=["cooperative", "competitive", "influence"], help="The social coupling model to use.")
    parser.add_argument("--coupling-strength", type=float, default=0.1, help="The strength of the social coupling.")
    parser.add_argument("--visualize", action="store_true", help="Visualize the phenomenal field of the agents.")

    args = parser.parse_args()

    # Create agents
    agents = [create_base_agent(f"agent_{i}") for i in range(args.num_agents)]

    # Create and run the simulation engine
    engine = SimulationEngine(agents, coupling_strength=args.coupling_strength)
    for epoch in range(args.epochs):
        engine.run_epoch(social_coupling_model=args.coupling_model)

    print("Simulation finished.")
    for i, agent in enumerate(agents):
        print(f"Final state of agent_{i}: {agent.omega_t}")

    # Visualize the results if requested
    if args.visualize:
        visualize_field(engine.phenomenal_field)

if __name__ == "__main__":
    main()
