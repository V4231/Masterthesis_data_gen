import plotly.graph_objects as go
from plotly.subplots import make_subplots
import glob
import numpy as np
import pandas as pd
from PIL import Image
import time

csv_files = [
            "input_picture.csv",
            #"output0.csv"
]
plot_names = ["Frequency unfiltered", "Frequency filtered"]
i = 0
data_frames = []

def read_csv(file,i,size,rest):
    df = pd.read_csv(file, skiprows=1, names=["CMD", "D0", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11", "D12", "D13", "D14", "D15", "TLAST", "TKEEP", "TIME_NS"])
    df.drop(columns=df.columns[0],axis=1, inplace=True)
    df.drop(columns=df.columns[df.shape[1]-1],axis=1, inplace=True)
    df.drop(columns=df.columns[df.shape[1]-1],axis=1, inplace=True)
    df.drop(columns=df.columns[df.shape[1]-1],axis=1, inplace=True)
    data_frames.append(df)
    #print(df)
    flattened_data = df.to_numpy().flatten()
    # Calculate square root of length
    square_arr = np.zeros(size*size)
    n = int(np.sqrt(len(flattened_data)))
    square_arr[:len(flattened_data)- rest] = flattened_data[:len(flattened_data)- rest]
    square_arr = square_arr.reshape((size, size)).astype('uint8')
    #print(square_arr)
    Image.fromarray(square_arr).save('output_pic'+ str(i) +'.jpeg')


for file in csv_files:
    read_csv(file,i,130,12)
    i = i + 1  

sim_file = '~/Documents/Masterthesis/workspace/build-vitis/aie_component/build/hw/aiesimulator_output/data/output0.csv'
for temp in range(90):
    read_csv(sim_file,i,128,0)
    time.sleep(20)