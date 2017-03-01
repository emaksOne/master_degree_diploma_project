import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

p1 = [0, 0, 0]
p2 = [5, 0, 0]
p3 = [5, 5, 0]
p4 = [0, 5, 0]

q1 = [0, 0, 5]
q2 = [5, 0, 5]
q3 = [5, 5, 5]
q4 = [0, 5, 5]

b1 = [2, 2, 2]
b2 = [3, 3, 3]

points = np.array([p1,p2,p3,p4,q1,q2,q3,q4,b1,b2])

plt.plot(points[:,0], points[:, 1], points[:,2], 'ro')
plt.show()