import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import sys

filename = sys.argv[1]

mpl.rcParams["agg.path.chunksize"] = 20000
data = np.loadtxt("data.txt")
clusterindex, centersnap = np.loadtxt(filename, unpack=True, dtype=int)
plt.axis("equal")
plt.axis("off")
plt.scatter(data[:, 0], data[:, 1], c=clusterindex)
snap = set(centersnap)
for i in snap:
    plt.scatter(data[i-1, 0], data[i-1, 1], marker='x')
plt.savefig(filename.split(".")[0] + ".png")
plt.show()
