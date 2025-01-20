import plotly.graph_objects as go
from plotly.subplots import make_subplots
import glob
import numpy as np
import csv

def create_csv(filename, num_rows, data):
    # Define the header
    header = ["CMD", "D", "D", "D", "D", "TLAST", "TKEEP"]

    # Add TLAST and TKEEP for every row
    tlast = np.zeros((num_rows, 1), dtype=np.int32)
    tkeep = -1 * np.ones((num_rows, 1), dtype=np.int32)

    # Add CMD column
    cmd_col = np.full((num_rows, 1), "DATA", dtype=object)

    # Combine CMD, data, TLAST, and TKEEP into a single array
    combined_data = np.concatenate([cmd_col, data, tlast, tkeep], axis=1)


    # Write to CSV
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write the header
        writer.writerows(combined_data)  # Write all rows

size = 1000
x = np.linspace(0, 1,size)

f = [10,20,30,40]
scaling = [2, 4, 0.3, 10]


y = np.random.rand(size,4)/scaling
for i in range(4):
    y[:,i] = y[:,i] + np.sin(x*2*np.pi*f[i])
    
    
create_csv("input_fir.csv", size, y)

