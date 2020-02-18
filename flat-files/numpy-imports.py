import numpy as np
import matplotlib.pyplot as plt

file = '../_datasets/digits.csv'
digits = np.loadtxt(file, delimiter=',')
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()
