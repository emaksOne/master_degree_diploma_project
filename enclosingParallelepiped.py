from __future__ import division
import scipy.spatial as sci
import numpy as np
import sympy as sp
from plotHelper import plotPoints
from plotHelper import plotConvexHull
import itertools
from sys import maxint
from convexHullHelper import analysConvexHull
from math import fabs

minVolume = maxint

def findMinimumEnclosingParallelepiped(points):
    convexHullModif = analysConvexHull(points)
    convexHull = sci.ConvexHull(points)
    verts = convexHullModif['vertices']
    neighbors = convexHullModif['neighbors']

    plotPoints(map(lambda x: points[x], verts))
    plotConvexHull(points, convexHull.simplices, 'k-')

    faces = convexHullModif['faces'].values()
    Ndict = {}
    N = []
    normalDict = {}

    def appendToN(item):
        key = item[0].equation()
        secondKey = item[1].equation()
        if key != secondKey:
            if key not in Ndict and secondKey not in Ndict:
                Ndict[key] = item

    def appendToNormals(plane, point):
        perpendicularLine = plane.perpendicular_line(point)
        planePoint = plane.intersection(perpendicularLine)[0]
        normalVector = sp.Point3D(point) - planePoint

        key = plane.equation()
        normalDict[key] = normalVector
        return normalVector


    for face in faces:
        p1 = sp.Point3D(points[face[0]])
        p2 = sp.Point3D(points[face[1]])
        p3 = sp.Point3D(points[face[2]])
        plane = sp.Plane(p1,p2,p3)
        maxDist = 0
        pMaxInd = 0
        for i in verts:
            point = sp.Point3D(points[i])
            currentDist = plane.distance(point)
            if(currentDist > maxDist):
                maxDist = currentDist
                pMaxInd = i
        normal = appendToNormals(plane, points[pMaxInd])
        paralelPlane = plane.parallel_plane(points[pMaxInd])
        entity = (plane, paralelPlane, normal)
        appendToN(entity)


    edges = convexHullModif['edges'].values()

    def isCorrectEdges(edge1, edge2):

        direction1 = sp.Point(edge1[1]) - sp.Point(edge1[0])
        direction2 = sp.Point(edge2[1]) - sp.Point(edge2[0])

        key1 = '{0}, {1}'.format(edge1[0], edge1[1])
        reverseKey1 = '{0}, {1}'.format(edge1[1], edge1[0])

        key2 = '{0}, {1}'.format(edge2[0], edge2[1])
        reverseKey2 = '{0}, {1}'.format(edge2[1], edge2[0])

        edgeNeighborsFor1 = neighbors.get(key1, neighbors.get(reverseKey1, []))
        edgeNeighborsFor2 = neighbors.get(key2, neighbors.get(reverseKey2, []))



        eqForFirst_1 = sp.Plane(points[edgeNeighborsFor1[0][0]], points[edgeNeighborsFor1[0][1]],
                                    points[edgeNeighborsFor1[0][2]]).equation()
        eqForFirst_2 = sp.Plane(points[edgeNeighborsFor1[1][0]], points[edgeNeighborsFor1[1][1]],
                                    points[edgeNeighborsFor1[1][2]]).equation()

        eqForSecond_1 = sp.Plane(points[edgeNeighborsFor2[0][0]], points[edgeNeighborsFor2[0][1]],
                                    points[edgeNeighborsFor2[0][2]]).equation()
        eqForSecond_2 = sp.Plane(points[edgeNeighborsFor2[1][0]], points[edgeNeighborsFor2[1][1]],
                                    points[edgeNeighborsFor2[1][2]]).equation()

        normalForFirst_1 = normalDict[eqForFirst_1]
        normalForFirst_2 = normalDict[eqForFirst_2]
        normalForSecond_1 = normalDict[eqForSecond_1]
        normalForSecond_2 = normalDict[eqForSecond_2]

        # for edge2
        dot1 = np.dot(direction2, normalForFirst_1)
        dot2 = np.dot(direction2, normalForFirst_2)

        if dot1 * dot2 >= 0:
            return False

        #for edge1
        dot1 = np.dot(direction1, normalForSecond_1)
        dot2 = np.dot(direction1, normalForSecond_2)

        if dot1 * dot2 >= 0:
            return False

        return True

    for i in range(len(edges)):
        for j in range(i+1,len(edges)):

            e1 = sp.Line3D(edges[i][0], edges[i][1])
            e2 = sp.Line3D(edges[j][0], edges[j][1])

            if not e1.is_parallel(e2) and isCorrectEdges(edges[i], edges[j]):
                normal = sp.Point3D(np.cross(e1.p2 - e1.p1, e2.p2 - e2.p1))

                plane = sp.Plane(e1.p1, normal_vector=normal)
                normal = appendToNormals(plane, e2.p1)
                paralelPlane = sp.Plane(e2.p1, normal_vector=normal)
                if plane.equation() != paralelPlane.equation():
                    entity = (plane, paralelPlane, normal)
                    appendToN(entity)


    N = Ndict.values()
    print 'N size = {0}'.format(len(N))

    minVolume = maxint
    supportingPlanes = ()


    i = 0

    for x, y, z in itertools.combinations(N, 3):
        print i
        i += 1
        en1 = x
        en2 = y
        en3 = z

        crossDot = calculateCrossDot(en1[2], en2[2], en3[2])
        if crossDot != 0:

            currentVolume = calculateVolume(en1[2], en2[2], en3[2], crossDot)

            if currentVolume < minVolume:
                minVolume = currentVolume
                print 'volume = {0}'.format(currentVolume)
                supportingPlanes = (en1[0], en1[1], en2[0], en2[1], en3[0], en3[1])

    print 'volume = {0}'.format(minVolume)

    return supportingPlanes[0],supportingPlanes[1], supportingPlanes[2], supportingPlanes[3], supportingPlanes[4], supportingPlanes[5]

def crossProduct(u, v):
    return (u[1]*v[2] -u[2]*v[1], u[2]*v[0] - u[0]*v[2], u[0]*v[1] - u[1]*v[0])

def dotProduct(u, v):
    return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]

def calculateCrossDot(n1, n2, n3):
    cross = crossProduct(n1, n2)
    dot = dotProduct(cross, n3)
    return dot


def calculateVolume(n1, n2, n3, crossDot):
    numerator = dotProduct(n1, n1) * dotProduct(n2, n2) * dotProduct(n3, n3)
    denominator = fabs(crossDot)
    volume = numerator/denominator
    return volume
