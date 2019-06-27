import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

np.random.seed(19680801)
N_points = 100000
n_bins = 20

# Generate a normal distribution, center at x=0 and y=5
x = np.random.randn(N_points)
y = .4 * x + np.random.randn(100000) + 5
np.random.seed(19680701)
z = np.random.randn(N_points) + 10
zz = 500000

fig, axs = plt.subplots(1, 4, sharey=True, tight_layout=True)

N, bins, patches = axs[0].hist(x, bins=n_bins)

plt.xlabel("1 2 3")
N1, bins1, patches1 = axs[1].hist(y, bins=n_bins)
axs[2].hist(z, bins=n_bins)
axs[3].hist(zz, bins=[1,2,3,4])

fracs = N / N.max()                                 
norm = colors.Normalize(fracs.min(), fracs.max())
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)


fracs = N1 / N1.max()
norm = colors.Normalize(fracs.min(), fracs.max())
for thisfrac, thispatch in zip(fracs, patches1):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

    
plt.show()
