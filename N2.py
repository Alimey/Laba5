from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
img = Image.open('бб.jpg').convert('RGB')
img_arr = np.asarray(img)

modified = img_arr.astype('float')
for i in range (0,1104):
    for k in range (0,736):
        modified[i][k][1] = modified[i][k][2]
        modified[i][k][0] = 0
modified[modified < 30] = 30
modified = modified.astype('uint8')

plt.imshow(modified)
plt.show()
