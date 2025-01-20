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

    empty = np.full((12), " ", dtype=object)

    data_arr = np.full((1), "DATA", dtype=object)

    tlast_keep_last = np.array([1,-1], dtype=np.int32)

    last_row = np.concatenate([data_arr, remain,empty, tlast_keep_last], axis=0)


    # Write to CSV
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write the header
        writer.writerows(combined_data)  # Write all rows
        writer.writerow(last_row)

image = Image.open("pepeLightbulb.jpg")

#print(image.size)

array_image = np.array(image.resize((130,130)).convert('L'))
Image.fromarray(array_image).save('resized_pepe.jpeg')
#image_plot = image.imread-('resized_pepe.jpeg')

#pyplot.imshow(image)
#pyplot.show()
print(array_image.shape)

flattened = array_image.flatten()

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
print(remaining_elements)

create_csv("input_picture.csv", full_array.shape[0],full_array,remaining_elements)
