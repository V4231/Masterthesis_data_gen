import plotly.graph_objects as go
from plotly.subplots import make_subplots
import glob
import numpy as np
import pandas as pd

csv_files = ["input_fir.csv", "output.csv"]

data_frames = []
for file in csv_files:
    df = pd.read_csv(file, skiprows=1, names=["CMD", "D0", "D1", "D2", "D3", "TLAST", "TKEEP", "TIME_NS"])
    df.drop(columns=df.columns[0],axis=1, inplace=True)
    df.drop(columns=df.columns[4],axis=1, inplace=True)
    df.drop(columns=df.columns[4],axis=1, inplace=True)
    df.drop(columns=df.columns[4],axis=1, inplace=True)
    data_frames.append(df)
    
size = 1000
x = np.linspace(0, 1,size)
colors = ["green", "red"]
fig = make_subplots(rows=4, cols=1)
for idx,df in enumerate(data_frames):
    i = 1
    for column_name, columns in df.items():
        fig.add_trace(
            go.Scatter(
                    x=x,
                    y=columns,
                    mode="lines",
                    name='Frequency ' + str(i),
                    marker=dict(color=colors[idx], size=10)
                ),
            row=i,
            col=1    
        )  
        i = i +1




fig.show()