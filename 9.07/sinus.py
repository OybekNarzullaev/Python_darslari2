import matplotlib.pyplot as plt
import numpy as np

# if using a jupyter notebook
# %matplotlib inline

x = np.arange(0, 4 * np.pi, 0.1)  # start,stop,step
y = np.sin(x)

plt.plot(x, y)
plt.show()
