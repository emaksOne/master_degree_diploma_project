from __future__ import division
import scipy.spatial as sci
import numpy as np
import sympy as sp
from plotHelper import plotPoints

from plotHelper import plotConvexHull

def findMinimumEnclosingParallelepiped(points):
    convexHull = sci.ConvexHull(points)
    print 'convex hull vertices are {0}'.format(convexHull.vertices)
    verts = convexHull.vertices
    plotPoints(map(lambda x: points[x], verts))
    plotConvexHull(points, convexHull.simplices, 'k-')

    faces = convexHull.simplices
    print 'faces is {0}'.format(faces)
    N = []

    for face in faces:
        p1 = sp.Point3D(points[face[0]])
        p2 = sp.Point3D(points[face[1]])
        p3 = sp.Point3D(points[face[2]])
        plane = sp.Plane(p1, p2, p3)
        maxDist = 0
        pMaxInd = 0
        for i in verts:
            point = sp.Point3D(points[i])
            currentDist = plane.distance(point)
            if(currentDist > maxDist):
                maxDist = currentDist
                pMaxInd = i

        paralelPlane = plane.parallel_plane(point)
        normal = plane.normal_vector
        entity = (plane, paralelPlane, normal)
        if entity not in N:
            N.append(entity)

    print N


