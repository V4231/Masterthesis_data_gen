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

num_rows = 100
# Generate data: 8 random fields per row
coefficents = coefficents = np.array([
    [10,5,30,20,46,3,8,100],
    [8,50,20,40,66,38,84,20],
    [1,50,90,60,67,43,58,90],
    [3,54,38,90,56,57,23,32]
    ])

#data = np.random.randint(-2**31, 2**31, size=(int(num_rows/2), 8), dtype=np.int32)
data = np.random.randint(1,2,size=(int(num_rows/2), 8), dtype=np.int32)
'''
data = np.array([
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1]
])
'''

#intermediate = data * coefficents

#golden = np.array(np.sum(intermediate,axis=0))

# Path for AIE
path = "../AIE_test/aie_component/data/"

# Generate Input data CSV
create_csv(path + "input0.csv", num_rows, data.reshape(num_rows,4))  # Vector type in AIE is 8 long, but 128 bit inputs --> split to 4 long vector

# Generate golden data CSV
#create_csv(path + "golden0.csv", 2, golden.reshape(2,4))  # Vector type in AIE is 8 long, but 128 bit inputs --> split to 4 long vector
