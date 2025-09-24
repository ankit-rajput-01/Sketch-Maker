import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

# ---- Image read karo ----
image = cv2.imread("C:/Users/TJC/Downloads/a1.jpg")

# ---- Convert to Gray ----
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ---- Invert image ----
inverted_image = 255 - gray_image

# ---- Blur image ----
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

# ---- Invert blurred ----
inverted_blurred = 255 - blurred

# ---- Create Pencil Sketch ----
sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

# ---- Animation: Dheere-dheere draw karo ----
plt.ion()   # interactive mode on
fig, ax = plt.subplots()
canvas = np.zeros_like(sketch)  # empty canvas (black image)

for i in range(0, sketch.shape[0], 2):   # har 2 rows me update karo (speed ke liye)
    canvas[i:i+2, :] = sketch[i:i+2, :]  # thoda thoda copy karo
    ax.clear()
    ax.imshow(canvas, cmap='gray')
    ax.axis("off")
    plt.draw()
    plt.pause(0.01)  # speed control (jitna chhota, utna fast)
    time.sleep(0.01)

plt.ioff()
plt.show()

# ---- Final sketch save ----
cv2.imwrite("seramata_slow_sketch.png", sketch)
