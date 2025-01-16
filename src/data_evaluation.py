import plotly.graph_objects as go

# Define a list of rectangles with their properties
# Each rectangle is defined as (x, y, width, height)
rectangles = [
    (1, 1, 2, 3),  # (x0, y0, width, height)
    (4, 2, 3, 1.5),
    (2, 5, 2.5, 2),
    (6, 6, 1.5, 1)
]

# Create a Plotly figure
fig = go.Figure()

# Add each rectangle as a shape
for rect in rectangles:
    x0, y0, width, height = rect
    x1, y1 = x0 + width, y0 + height  # Calculate opposite corner
    fig.add_shape(
        type="rect",
        x0=x0, y0=y0, x1=x1, y1=y1,
        line=dict(color="blue"),  # Border color
        fillcolor="lightblue",  # Fill color
        opacity=0.5             # Transparency
    )

# Update layout to set axis limits
fig.update_layout(
    title="Rectangle Visualization",
    xaxis=dict(title="X-axis", range=[0, 10]),
    yaxis=dict(title="Y-axis", range=[0, 10]),
    showlegend=False
)

# Display the plot
fig.show()
