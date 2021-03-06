from __future__ import division
import scipy.spatial as sci
import numpy as np
import sympy as sp
from plotHelper import plotPoints
from plotHelper import plotConvexHull
import itertools
from sys import maxint


def get2Dpoints(points):
    zZeroPlane = sp.Plane((0, 0, 0), (1, 0, 0), (1, 1, 0))
    xZeroPlane = sp.Plane((0, 0, 0), (0, 1, 0), (0, 1, 1))
    currentPlane = sp.Plane(points[0], points[1], points[2])
    points = np.array(points)
    if currentPlane.is_perpendicular(zZeroPlane):
        if currentPlane.is_perpendicular(xZeroPlane):
            return points[:, [0, 2]]
        return points[:, [1, 2]]
    else:
        return points[:, [0, 1]]

def analysConvexHull(points):
    print 'start prepere convex hull stuff'
    faces = {}
    edges = {}
    neighbors = {}
    convexHull = sci.ConvexHull(points)

    for i in range(0, len(convexHull.equations)):
        equation = convexHull.equations[i]
        key = ','.join(str(v) for v in equation)
        val = faces.get(key, [])
        val.extend(convexHull.simplices[i])
        faces[key] = val

    facesValues = faces.values()

    for i in range(0, len(facesValues)):
        facePoints3D = map(lambda x: points[x], facesValues[i])
        facePoints2D = get2Dpoints(facePoints3D)
        faceHull = sci.ConvexHull(facePoints2D)

        for j in range(0, len(faceHull.simplices)):
            edge = faceHull.simplices[j]
            key = '{0}, {1}'.format(facePoints3D[edge[0]],facePoints3D[edge[1]])
            reverseKey = '{0}, {1}'.format(facePoints3D[edge[1]],facePoints3D[edge[0]])
            if key not in edges and reverseKey not in edges:
                edges[key] = (facePoints3D[edge[0]], facePoints3D[edge[1]])

            val = neighbors.get(key, [])
            reverseVal = neighbors.get(reverseKey, [])

            if key not in neighbors and reverseKey not in neighbors:
                neighbors[key] = [facesValues[i]]
            if key in neighbors:
                val = neighbors[key]
                if val[0] != facesValues[i]:
                    val.append(facesValues[i])
                neighbors[key] = val
            else:
                reverseVal = neighbors[reverseKey]
                if reverseVal[0] != facesValues[i]:
                    reverseVal.append(facesValues[i])
                neighbors[reverseKey] = reverseVal

    return {'faces': faces, 'edges': edges, 'neighbors': neighbors, 'vertices': convexHull.vertices}





