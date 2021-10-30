import matplotlib.pyplot as plt
import numpy as np

rong = np.array([170,184,174,185,145,146,156,174,165,149,192])
dai= np.array([  89,  67, 85,77, 88, 96, 53, 68 ,98, 81, 75])

plt.xlim(140,200)
plt.ylim(50,100)
plt.scatter(rong,dai)
plt.title("Scatter Plot")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()