import pandas as pd
import plotly.graph_objects as go
import glob
import os
import numpy as np

def plot_timeline_with_rectangles(folder_path):
    """
    Reads all CSV files in the given folder, combines their data,
    and plots a 1D timeline with rectangles marking events.

    Parameters:
    folder_path (str): Path to the folder containing the CSV files.
    """
    # Read all CSV files in the folder
    csv_files = glob.glob(f"{folder_path}/*.csv")

    file_names = []

    if not csv_files:
        print("No CSV files found in the folder!")
        return
    
    data_frames = []
    
    for file in csv_files:
        file_names.append(os.path.split(file)[1].replace(".csv",""))
        df = pd.read_csv(file, skiprows=1, names=["CMD", "D0", "D1", "D2", "D3", "TLAST", "TKEEP", "TIME_NS"])
        data_frames.append(df)
    
    # Plot the timeline with rectangles
    fig = go.Figure()
    
    # Define height and width of rectangles
    x_max = 2000
    offset = 0.2

    pl_clock_frequency = 0.325
    pl_clock_duration = 1/ pl_clock_frequency
    aie_clock_frequency = 1.25
    aie_clock_duration = 1 / aie_clock_frequency
    time_points = []
    clock_points = []

    t = 0
    while t < x_max:
        # Add the time for the low and high states
        time_points.extend([t, t + aie_clock_duration / 2])
        clock_points.extend([1, 0])  # Low, then high
        t += aie_clock_duration


    fig.add_trace(go.Scatter(
            x=time_points,
            y=clock_points,
            mode="lines",
            line_shape='hv',  # Step-like lines
            name='Clock Signal',
            marker=dict(color="green", size=10))
    )

    x = 0
    y = 1 + offset
    colors = ['blue', 'yellow', 'blue', 'yellow']
    for idx,df in enumerate(data_frames):
    #for idx, time in enumerate(combined_df['TIME_NS']):
        # Add a rectangle at each time
        for nah,row in df.iterrows():
            for i in range(4):
                fig.add_shape(
                    type="rect",
                    x0=row['TIME_NS'], y0= y + i, x1=row['TIME_NS']+ pl_clock_duration, y1=y + i + 1,
                    line=dict(color=colors[idx]),  # Border color
                    fillcolor=colors[idx],  # Fill color
                    opacity=0.5             # Transparency
                )
                fig.add_annotation(
                    x=row['TIME_NS'] + pl_clock_duration / 2 , y= y + i + 0.5,
                    text=row['D'+str(i)],
                    showarrow=False
                )

        fig.add_annotation(
            x=30, y= y,
            text=file_names[idx],
            showarrow=False
        )       
        y = y + 4 + offset

        fig.add_trace(go.Scatter(
            x=[0, x_max],
            y=[y, y],
            mode="lines",
            marker=dict(color="red", size=10))
        )
        y = y + offset
    
    # Adjust plot limits and labels
    #plt.xlim(combined_df['TIME_NS'].min() - 5, combined_df['TIME_NS'].max() + 5)
    fig.update_layout(
        title="Rectangle Visualization",
        xaxis=dict(title="X-axis", range=[0, x_max]),
        yaxis=dict(title="Y-axis", range=[0, y]),
        showlegend=False
    )
    fig.show()

# Example usage:
# Specify the folder containing your CSV files
folder_path = "../AIE_test/aie_component/build/hw/aiesimulator_output/data/"
folder_path="data/"
plot_timeline_with_rectangles(folder_path)