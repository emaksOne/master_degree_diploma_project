import scipy.spatial as sci
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import itertools
import sys
print sys.maxint

t = []
f = [[6,2,1]]
t.extend(f)
print t
t = list(set(t))
print t
points = np.random.rand(30, 2)

point = sp.Point3D([6,5,4])
point2 = sp.Point3D([5,4,3])
print point - point2
print point
e1 = sp.Line3D((0,5,0), (5,5,0))
e2 = sp.Line3D((5,5,0), (0,5,0))

print e1.direction_ratio
print e2.p1

print range(10)
print range(1,10)

print sp.geometry.intersection(e1,e2)

normal = sp.Point3D(np.cross(e1.p2-e1.p1, e2.p2-e2.p1))
print normal
print e1.p1
plane = sp.Plane(e1.p1, normal_vector=normal)


print plane


for subset in itertools.combinations([1,2,3], 2):
    print subset
collection = []
l1 = sp.Line3D(sp.Point3D(0,0,0), sp.Point3D(1,1,0))
l2 = sp.Line3D(sp.Point3D(2,2,0), sp.Point3D(3,3,0))
print l1.equation()
print l2.equation()
collection.append(l1)

if l2 not in collection:
    collection.append(l2)

print collection



line1 = sp.Line3D(sp.Point3D(0,0,0), sp.Point3D(1,0,0))
line2 = sp.Line3D(sp.Point3D(0,1,0), sp.Point3D(2,2,1))
line3 = sp.Line3D(sp.Point3D(0,0,1), sp.Point3D(1,0,1))

print sp.Line3D.is_parallel(line2, line3)
# tuple = (0, 0, 1)
#
# p1 = sp.Point(tuple)
# print p1.distance((1,2,3))
#
# listA = [i for i in range(10)]
# print listA
#
# listB = [i for i in listA if i not in (2,5)]
# print listB
#
# print p1

p11, p22 = sp.Point(0, 0, 0), sp.Point(1, 1, 1)

s = sp.Line3D(p11, p22)

targ = sp.Point(-1,1,1)

print s.distance(targ)

distan = s.distance(targv)
print distan

po1 = sp.Point(255, 252, 255)
po2 = sp.Point(0, 8, 0)

li = sp.Line(po1, po2)

dist = li.distance(sp.Point(180,173))
print li

p1,p2,p3,p4, k1,k2,k3,k4 = sp.Point(0,0,0), sp.Point(1,0,0), sp.Point(1,1,0), sp.Point(0,1,0), \
                           sp.Point(0,0,1), sp.Point(1,0,1), sp.Point(1,1,1), sp.Point(0,1,1)

points = [p1, p2, p3, p4, k1, k2, k3, k4]

print 'find min point by x'
startPoint = min(points, key=lambda x: x[0])
print 'minPoint = {0}'.format(startPoint)


plDown = sp.Plane(p1,p2,p3)
print plDown
plFront = sp.Plane(p1,p2, k1)
print plFront
plLeft = sp.Plane(p1, p4, k1)
print plLeft

intersectLine = plDown.intersection(plFront)
print intersectLine

m1 = plLeft.intersection(plDown.intersection(plFront)[0])
print m1





