import plotly.graph_objects as go

def visualize_field(phenomenal_field):
    """
    Generates a 3D scatter plot of the Autonic Phenomenal Field for all agents.
    """
    fig = go.Figure()

    agent_ids = set()
    for t, agent_data in phenomenal_field.field_data.items():
        for agent_id in agent_data.keys():
            agent_ids.add(agent_id)

    for agent_id in sorted(list(agent_ids)):
        agent_states = []
        for t, agent_data in phenomenal_field.field_data.items():
            if agent_id in agent_data:
                agent_states.append(agent_data[agent_id])

        if not agent_states:
            continue

        # For visualization purposes, we'll just use the first 3 dimensions of the state.
        x_coords = [state[0] for state in agent_states]
        y_coords = [state[1] for state in agent_states]
        z_coords = [state[2] for state in agent_states]
        time_steps = list(range(len(agent_states)))

        fig.add_trace(go.Scatter3d(
            x=x_coords,
            y=y_coords,
            z=z_coords,
            mode='lines+markers',
            marker=dict(
                size=5,
                color=time_steps,
                colorscale='Viridis',
                opacity=0.8
            ),
            line=dict(
                width=2
            ),
            name=agent_id
        ))

    fig.update_layout(
        title="Autonic Phenomenal Field",
        scene=dict(
            xaxis_title='Dimension 1',
            yaxis_title='Dimension 2',
            zaxis_title='Dimension 3'
        )
    )
    fig.show()
