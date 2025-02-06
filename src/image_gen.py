from PIL import Image
import numpy as np
import csv

def create_csv(filename, num_rows, data, remain):
    # Define the header
    header = ["CMD", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "TLAST", "TKEEP"]

    # Add TLAST and TKEEP for every row
    tlast = np.zeros((num_rows, 1), dtype=np.int32)
    tkeep = -1 * np.ones((num_rows, 1), dtype=np.int32)

    # Add CMD column
    cmd_col = np.full((num_rows, 1), "DATA", dtype=object)

    # Combine CMD, data, TLAST, and TKEEP into a single array
    combined_data = np.concatenate([cmd_col, data, tlast, tkeep], axis=1)

    remaining_data = np.full((16), 0, dtype=object)

    remaining_data[0:remain.shape[0]] = remain

    data_arr = np.full((1), "DATA", dtype=object)

    tlast_keep_last = np.array([1,"0xFF"], dtype=object)

    last_row = np.concatenate([data_arr, remaining_data, tlast_keep_last], axis=0)


    # Write to CSV
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write the header
        writer.writerows(combined_data)  # Write all rows
        writer.writerow(last_row)

def create_hls_buffer(filename,data):
    with open(filename,mode="w",newline="") as file:
        writer =    csv.writer(file)
        writer.writerow(data)

image = Image.open("test_pic1.jpeg")

#print(image.size)

array_image = np.array(image.resize((66,66)).convert('L'))
Image.fromarray(array_image).save('resized_pepe.jpeg')
#image_plot = image.imread-('resized_pepe.jpeg')

#pyplot.imshow(image)
#pyplot.show()
print(array_image.shape)

flattened = array_image.flatten()
dummy_Data = np.eye(18,dtype=np.uint8) *255
#flattened = dummy_Data.flatten()
#flattened = np.arange(1024,dtype=np.uint8)
#flattened = np.ones(400,dtype=np.uint8)
columns = 16

# Calculate how many complete rows can be made
num_complete_rows = len(flattened) // columns

# Reshape into a full array with complete rows
full_array = flattened[:num_complete_rows * columns].reshape(-1, columns)

# Store the remaining elements in a separate array
remaining_elements = flattened[num_complete_rows * columns:]

print("Full Array:")
print(full_array.shape[0])
print("\nRemaining Elements:")
print(remaining_elements.shape)

#create_hls_buffer("data_hls.csv",flattened)

#create_csv("input_picture.csv", full_array.shape[0],full_array,remaining_elements)
