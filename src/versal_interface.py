import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import serial
import pandas as pd
import threading
import time

# Configure serial port (Change 'COM3' or '/dev/ttyUSB0' to your port)
SERIAL_PORT = '/dev/pts/14'  # Change this based on your system
BAUD_RATE = 115200

# Open the serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# Data storage
data = {"time": [], "value": []}
start_time = time.time()

# Function to read serial data in a separate thread
def read_serial():
    print("hello")
    global data
    while True:
        try:
            #line = ser.readline().decode("utf-8").strip()  # Read line from serial
            line = ser.readline()
            print(line)
            if line:
                timestamp = time.time() - start_time
                data["time"].append(timestamp)
                data["value"].append(float(line))

                # Keep only the last 100 data points for performance
                if len(data["time"]) > 100:
                    data["time"].pop(0)
                    data["value"].pop(0)

        except Exception as e:
            print("Error reading serial:", e)

read_serial()
'''
# Start serial reading in a background thread
thread = threading.Thread(target=read_serial, daemon=True)
thread.start()

# Dash app setup
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Real-Time Serial Data Plot"),
    dcc.Graph(id='live-graph'),
    dcc.Interval(id='interval-component', interval=200, n_intervals=0)  # Update every 200ms
])

@app.callback(
    Output('live-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph(n):
    df = pd.DataFrame(data)

    return {
        'data': [go.Scatter(
            x=df["time"], 
            y=df["value"], 
            mode='lines+markers'
        )],
        'layout': go.Layout(
            title="Live Data",
            xaxis=dict(title="Time (s)"),
            yaxis=dict(title="Value"),
            margin=dict(l=40, r=40, t=40, b=40)
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)
    '''
