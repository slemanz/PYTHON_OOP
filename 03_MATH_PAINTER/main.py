import numpy as np
from PIL import Image

# Create 3d numpy array of zeros, then replace zeros (black, pixels) with yellow pixels
data = np.zeros((100, 100, 3), dtype=np.uint8)
data[:] = [255,255, 0]

# Make a red patch
data[20:60, 20:60] = [255, 0, 0]
data[20:60, 20:60] = [255, 0, 0]

data[70:80, 70:80] = [0, 255, 0]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')