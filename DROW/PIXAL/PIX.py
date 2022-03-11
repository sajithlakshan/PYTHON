from PIL import Image
import numpy as np

w, h = 512, 512
data = np.zeros((h, w, 4), dtype=np.uint8)
for Y in range(h):
    for X in range(w):
      data[Y, X] = [255,126,22,255] # red patch in upper left  data[Y, X] = [R, G, B,A]
img = Image.fromarray(data, 'RGBA')
img.save('my.png')
img.show()
