import scipy.spatial as sci
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


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





