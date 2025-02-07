from dash import Dash, dcc, html, Input, Output
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from collections import deque
import serial

X = range(100)
Y = deque(maxlen=100)
Y.append(1)

# Configure serial port (Change 'COM3' or '/dev/ttyUSB0' to your port)
SERIAL_PORT = '/dev/pts/8'  # Change this based on your system
BAUD_RATE = 115200

# Open the serial connection
#ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# Function to read serial data in a separate thread
def read_serial():
    global data
    try:
        line = ser.readline().decode("utf-8").strip()  # Read line from serial
        return line

    except Exception as e:
        print("Error reading serial:", e)

app = Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True,style={'width': '90vh', 'height': '90vh'}),
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
    #Y.append(float(read_serial()))
    Y.append(1)
    fig = make_subplots(rows = 4, cols =1)
    for i in range(1,5):
        fig.add_trace(
                go.Scatter(
                    x=list(X),
                    y=list(Y),
                    name='Scatter',
                    mode= 'lines+markers' 
                ),
                row=i,
                col=1    
        )

    return fig
    #return {'data': [fig],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
    #                                            yaxis=dict(range=[-2,2]),)}



if __name__ == '__main__':
    app.run_server(debug=True)