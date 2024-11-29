import numpy as np
import matplotlib.pyplot as plt

# Image dimensions
width, height = 128, 128

# Create a blank image (all white background)
image = np.full((height, width, 3), [255, 255, 255], dtype=np.uint8)

# Define colors
green = [34, 139, 34]   # Leaves: Forest Green
brown = [139, 69, 19]   # Trunk: Saddle Brown
red = [255, 0, 0]       # Apples: Bright Red

# Draw the tree trunk
trunk_width = width // 8
trunk_height = height // 4
trunk_x_start = (width - trunk_width) // 2
trunk_y_start = height - trunk_height
image[trunk_y_start:, trunk_x_start:trunk_x_start+trunk_width] = brown

# Draw the tree canopy (circle for simplicity)
canopy_radius = width // 4
canopy_center = (height // 2, width // 2)

for y in range(height):
    for x in range(width):
        # Equation of a circle: (x - center_x)^2 + (y - center_y)^2 < radius^2
        if (x - canopy_center[1])**2 + (y - canopy_center[0])**2 < canopy_radius**2:
            image[y, x] = green

# Add apples (random positions in the canopy)
np.random.seed(42)  # For reproducible results
num_apples = 20
for _ in range(num_apples):
    apple_x = np.random.randint(canopy_center[1] - canopy_radius, canopy_center[1] + canopy_radius)
    apple_y = np.random.randint(canopy_center[0] - canopy_radius, canopy_center[0] + canopy_radius)
    # Ensure the apple is within the canopy
    if (apple_x - canopy_center[1])**2 + (apple_y - canopy_center[0])**2 < canopy_radius**2:
        # Draw the apple (a small 3x3 red square for simplicity)
        image[max(apple_y-1, 0):min(apple_y+2, height), max(apple_x-1, 0):min(apple_x+2, width)] = red

print(image)
# Plot the image
plt.imshow(image)
plt.axis('off')
plt.title("Apple Tree")
plt.show()
