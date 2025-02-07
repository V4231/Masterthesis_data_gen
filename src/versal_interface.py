from dash import Dash, dcc, html, Input, Output
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from collections import deque
import serial
import time
import numpy as np

X = np.arange(61)
#Y = deque(maxlen=100)
#Y.append((1,1,1,1))
Y = np.zeros((61,4))

# Configure serial port (Change 'COM3' or '/dev/ttyUSB0' to your port)
SERIAL_PORT = '/dev/pts/9'  # Change this based on your system
BAUD_RATE = 115200

# Open the serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# Function to read serial data in a separate thread
def read_serial():
    try:
        line = ser.readline().decode("utf-8").strip()  # Read one line, decode, and strip spaces
        if line:  # Ensure line is not empty
            return np.array([float(i) for i in line.split(',')])  # Convert to NumPy array
    except ValueError:
        print("Received invalid data, skipping...")
    except Exception as e:
        print("Error reading serial:", e)
    
    return np.zeros(4)  # Return a default value in case of an error

'''
while(True):
    #print(Y)
    #Y = np.roll(Y,-1,axis=0)
    try:
        print(read_serial())
        #Y[-1,:] = read_serial()
        #Y[-1,:] = read_serial()
    except:
        print("Not valid read")    
    time.sleep(0.005)


'''
app = Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True,style={'width': '90vh', 'height': '90vh'}),
        dcc.Interval(
            id='graph-update',
            interval=1*100
        ),
    ]
)

@app.callback(Output('live-graph', 'figure'),
              Input('graph-update', 'n_intervals')
)
def update_graph_scatter(n):
    global Y
    Y[-1,:] = read_serial()
    #Y.append(1)
    fig = make_subplots(rows = 4, cols =1)
    for i in range(4):
        fig.add_trace(
                go.Scatter(
                    x=X,
                    y=Y[:,i],
                    name='Scatter',
                    mode= 'lines' 
                ),
                row=i+1,
                col=1    
        )
    Y = np.roll(Y,-1,axis=0)
    fig.update_xaxes(range=[0, 61])
    fig.update_yaxes(range=[-1.2, 1.2])    
    return fig
    #return {'data': [fig],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
    #                                            yaxis=dict(range=[-2,2]),)}



if __name__ == '__main__':
    app.run_server(debug=True)
