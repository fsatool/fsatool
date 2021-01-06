import numpy as np
import matplotlib.pyplot as plt
import sys
import scipy.ndimage
from scipy import interpolate

filename = sys.argv[1]
bins_x = int(sys.argv[2])
bins_y = int(sys.argv[3])


#plt.style.use("paper")
cmap = plt.cm.get_cmap("nipy_spectral")
pot,x,y = np.loadtxt(filename, skiprows=3, usecols=(0,2,3), unpack=True)
x = x.reshape(bins_x, bins_y)
y = y.reshape(bins_x, bins_y)
pot = pot.reshape(bins_x, bins_y)

nonzero = pot.nonzero()
pot[pot==0] = np.inf
if len(pot[nonzero]) != 0:
    pot[nonzero] -= np.min(pot[nonzero])

#f = interpolate.interp2d(x,y, pot, kind ="cubic")
#pot = f(x, y)
#x = np.linspace(0, 11, 100)
#y = np.linspace(0, 15, 100)
#x, y = np.meshgrid(x, y)

plt.xlabel(r"DISTANCE1 (\AA)")
plt.ylabel(r"DISTANCE2 (\AA)")
#plt.ylim(0.1, 18)
cnt = plt.contourf(x,y,pot,100,cmap=cmap, interpolation="bicubic")
for c in cnt.collections:
    c.set_edgecolor("face")
#plt.contourf(pot,100,cmap=cmap)
#plt.imshow(x,y,pot, cmap=cmap, interpolation="bicubic")
bar = plt.colorbar()
bar.set_label("Free energy (kcal/mol)")
plt.tight_layout()
plt.savefig("biasing potential.pdf")
plt.show()
