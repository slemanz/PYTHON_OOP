import numpy as np
from PIL import Image

# Create 3d numpy array of zeros, then replace zeros (black, pixels) with yellow pixels
data = np.zeros((1000, 1000, 3), dtype=np.uint8)
data[:] = [255,255, 0]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')