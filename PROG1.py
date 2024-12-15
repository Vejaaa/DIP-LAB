#1
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = cv2.imread('/content/imafes.jpg')

# Display original image using Matplotlib
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for proper color display
plt.title('Original Image')
plt.axis('off')
plt.show()

# Convert image to a NumPy array
newimg = np.asarray(img)
X, Y, D = newimg.shape

# Divide the image into quadrants
div1 = X // 2
div2 = Y // 2
top_left = newimg[:div1, :div2]
top_right = newimg[:div1, div2:]
bottom_left = newimg[div1:, :div2]
bottom_right = newimg[div1:, div2:]

# Store quadrants in a list
div_img = [top_left, top_right, bottom_left, bottom_right]

# Plot the quadrants
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
for idx, ax in enumerate(axs.flat):
    ax.imshow(cv2.cvtColor(div_img[idx], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for proper color display
    ax.set_title(f'Quadrant {idx+1}: {div_img[idx].shape}')
    ax.axis('off')

plt.tight_layout()
plt.show()

