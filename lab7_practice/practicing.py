import numpy as np
import matplotlib.pyplot as plt
import imageio.v3 as iio
import ipympl
import skimage as ski

img = np.random.rand(3,4,3)
img.shape
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('image')
plt.imshow(img)