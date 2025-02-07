import plotly.graph_objects as go
from plotly.subplots import make_subplots
import glob
import numpy as np
import pandas as pd

df = pd.read_csv("data_in/output_hls.csv",header=0)

#print(df['DATA'])

x = np.arange(df.shape[0])
#x = np.arange(100)/100
#y=df['DATA']
#y = np.sin(x * 2* np.pi)
#print(y)
fig = make_subplots(
                    rows=4, cols=1
)
'''
fig.add_trace(
    go.Scatter(
            x=x,
            y=y,
            mode="lines"
        )
    
)
'''
i = 1
for column_name, columns in df.items():
    fig.add_trace(
        go.Scatter(
                x=x,
                y=columns,
                mode="lines",
                name=column_name,
                marker=dict(color='green', size=10)
            ),
        row=i,
        col=1    
    )
    i = i +1

fig.update_xaxes(range=[0, df.shape[0]])
fig.update_yaxes(range=[-1.2, 1.2])
fig.show()