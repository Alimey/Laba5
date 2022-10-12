import numpy as np
gradient = np.tile(np.arange(0, 256, dtype='uint8'), (255, 1))

import matplotlib.pyplot as plt
plt.imshow(gradient, cmap ='hot', vmin=32, vmax=255)
plt.show()