import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import serial

X = range(100)
Y = deque(maxlen=100)
Y.append(1)

# Configure serial port (Change 'COM3' or '/dev/ttyUSB0' to your port)
SERIAL_PORT = '/dev/pts/8'  # Change this based on your system
BAUD_RATE = 115200

# Open the serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# Function to read serial data in a separate thread
def read_serial():
    global data
    try:
        line = ser.readline().decode("utf-8").strip()  # Read line from serial
        return line

    except Exception as e:
        print("Error reading serial:", e)

app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1*1000
        ),
    ]
)

@app.callback(Output('live-graph', 'figure'),
              Input('graph-update', 'n_intervals')
)
def update_graph_scatter(n):
    Y.append(float(read_serial()))

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[-2,2]),)}



if __name__ == '__main__':
    app.run_server(debug=True)