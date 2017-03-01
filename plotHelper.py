import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def plotPoints(points, color='bo'):
    points = np.array(points)
    plt.plot(points[:,0],points[:,1], points[:,2], color)

def plotConvexHull(points, simplices, color):
    points = np.array(points)
    for simplex in simplices:
        simplex = np.array(simplex)
        plt.plot(points[simplex, 0], points[simplex, 1], points[simplex, 2], color)

def showPlot():
    plt.show()


