from __future__ import division
import scipy.spatial as sci
import numpy as np
import sympy as sp
from plotHelper import plotPoints
from plotHelper import plotConvexHull
import itertools
from sys import maxint

def optimizeAlgorithm(points):
    convexHull = sci.ConvexHull(points)
    print 'convex hull vertices are {0}'.format(convexHull.vertices)
    verts = convexHull.vertices

    plotPoints(map(lambda x: points[x], verts))
    plotConvexHull(points, convexHull.simplices, 'k-')

    faces = convexHull.simplices
    edgesDict = {}
    edges = []
    print 'faces size is {0}'.format(len(faces))
    N = []

    for face in faces:

        addLines(face, edgesDict)

    print 'edges size is {0}'.format(len(edgesDict))
    edges = edgesDict.values()

    for i in range(len(edges)):
        direction1 = edges[i].direction_ratio
        for j in range(i+1, len(edges)):
            direction2 = edges[j].direction_ratio
            dot2 = np.dot(direction1, direction2)
            if dot2 != 0:
                continue
            module2 = np.dot(direction2, direction2)
            for k in range(j+1, len(edges)):
                direction3 = edges[k].direction_ratio
                dot3 = np.dot(direction3, direction2)
                if dot3 != 0:
                    continue
                module3 = np.dot(direction3, direction3)
                direction1 = np.cross(direction3, direction2)
                module1 = module3 * module2

                vMin = [0,0,0]
                vMax = [0,0,0]
                startV = verts[0]
                for m in verts:
                    diff = points[m] - points[startV]
                    for c in range(3):




def addLines(face, edgeDict):
    p1 = sp.Point3D(points[face[0]])
    p2 = sp.Point3D(points[face[1]])
    p3 = sp.Point3D(points[face[2]])
    for p1,p2 in itertools.combinations(points, 2):
        line = sp.Line3D(p1, p2)
        key = '{0},{1}'.format(p1,p2)
        reverseKey = '{0},{1}'.format(p2,p1)
        # if line not in edges:
        #     edges.append(line)
        if key not in edgeDict and reverseKey not in edgeDict:
            edgeDict[key] = line
