
from scipy.spatial import ConvexHull
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform

import matplotlib.pyplot as plt
import numpy as np

test = np.array([[0,0],[0,1], [0,2], [0,4]])
print test





points = np.random.rand(3, 2)

dist = squareform(pdist(test))

farhest_points = dist.argmax(axis=0)

tuple = np.unravel_index(dist.argmax(), dist.shape)
print tuple

print farhest_points
print points
print (dist)


