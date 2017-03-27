from __future__ import division
import scipy.spatial as sci
import numpy as np
import sympy as sp
from plotHelper import plotPoints
from plotHelper import plotConvexHull
import itertools
from sys import maxint
from convexHullHelper import analysConvexHull
from sympy import are_similar

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
        #normalVector = perpendicularLine.p2 - perpendicularLine.p1
        planePoint = plane.intersection(perpendicularLine)[0]
        normalVector = sp.Point3D(point) - planePoint

        key = plane.equation()
        normalDict[key] = normalVector


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
        appendToNormals(plane, points[pMaxInd])
        paralelPlane = plane.parallel_plane(points[pMaxInd])
        normal = plane.normal_vector
        entity = (plane, paralelPlane, normal)
        # if entity not in N:
        #     N.append(entity)
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

        # normalForFirst_1 = sp.Plane(points[edgeNeighborsFor1[0][0]], points[edgeNeighborsFor1[0][1]], points[edgeNeighborsFor1[0][2]]).normal_vector
        # normalForFirst_2 = sp.Plane(points[edgeNeighborsFor1[1][0]], points[edgeNeighborsFor1[1][1]], points[edgeNeighborsFor1[1][2]]).normal_vector
        #
        # normalForSecond_1 = sp.Plane(points[edgeNeighborsFor2[0][0]], points[edgeNeighborsFor2[0][1]],
        #                             points[edgeNeighborsFor2[0][2]]).normal_vector
        # normalForSecond_2 = sp.Plane(points[edgeNeighborsFor2[1][0]], points[edgeNeighborsFor2[1][1]],
        #                             points[edgeNeighborsFor2[1][2]]).normal_vector

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
        # if dot1 == 0 and dot2 == 0:
        #     return True
        if dot1 * dot2 >= 0:
            return False

        #for edge1
        dot1 = np.dot(direction1, normalForSecond_1)
        dot2 = np.dot(direction1, normalForSecond_2)
        # if dot1 == 0 and dot2 == 0:
        #     return True
        if dot1 * dot2 >= 0:
            return False

        return True



    #print 'N size = {0}'.format(len(N))

    for i in range(len(edges)):
        #print 'i = {0}'.format(i)
        for j in range(i+1,len(edges)):
            #print 'j = {0}'.format(j)
            # e1 = edges[i][0]
            # e2 = edges[j][0]
            # if not e1.is_parallel(e2):
            #     if isCorrectEdge(e1) and isCorrectEdge(e2):
            #         normal = sp.Point3D(np.cross(e1.p2 - e1.p1, e2.p2 - e2.p1))
            #         #if isCorrect(e1, normal) and isCorrect(e2, normal):
            #         plane = sp.Plane(e1.p1, normal_vector=normal)
            #         paralelPlane = sp.Plane(e2.p1, normal_vector=normal)
            #         if plane.equation() != paralelPlane.equation():
            #             entity = (plane, paralelPlane, normal)
            #             if entity not in N:
            #                 N.append(entity)
            e1 = sp.Line3D(edges[i][0], edges[i][1])
            e2 = sp.Line3D(edges[j][0], edges[j][1])

            if not e1.is_parallel(e2) and isCorrectEdges(edges[i], edges[j]):
                normal = sp.Point3D(np.cross(e1.p2 - e1.p1, e2.p2 - e2.p1))
                plane = sp.Plane(e1.p1, normal_vector=normal)
                paralelPlane = sp.Plane(e2.p1, normal_vector=normal)
                if plane.equation() != paralelPlane.equation():
                    entity = (plane, paralelPlane, normal)
                    #N.append(entity)
                    appendToN(entity)


    N = Ndict.values()
    print 'N size = {0}'.format(len(N))

    minVolume = maxint
    supportingPlanes = ()

    # for i in range(len(N)):
    #     #print 'i = {0}'.format(i)
    #     for j in range(i+1, len(N)):
    #         #print 'j = {0}'.format(j)
    #         for k in range(j+1, len(N)):
    #             en1 = N[i]
    #             en2 = N[j]
    #             en3 = N[k]
    #             line1 = sp.Line3D((0,0,0), en1[2])
    #             line2 = sp.Line3D((0,0,0), en2[2])
    #             line3 = sp.Line3D((0,0,0), en3[2])
    #             #if line1.is_perpendicular(line2) and line2.is_perpendicular(line3) and line1.is_perpendicular(line3):
    #             #if line1.is_perpendicular(line2) and line2.is_perpendicular(line3):
    #             if np.cross(line2.p2-line2.p1, line1.p2 - line1.p1).dot(line3.p2 - line3.p1) != 0:
    #                 a = en1[0].distance(en1[1])
    #                 b = en2[0].distance(en2[1])
    #                 c = en3[0].distance(en3[1])
    #                 currentVolume = a*b*c
    #                 #if currentVolume == 125/2:
    #                  #   print 'hop'
    #
    #                 print 'volume = {0}'.format(currentVolume)
    #
    #                 if currentVolume < minVolume:
    #                     minVolume = currentVolume
    #                     supportingPlanes = (en1[0], en1[1], en2[0], en2[1], en3[0], en3[1])
    #print 'itertools size is {0}'.format(itertools.product(N, repeat = 3))
    i = 0
    for x, y, z in itertools.combinations(N,3):
        print i
        i += 1
        en1 = x
        en2 = y
        en3 = z
        line1 = sp.Line3D((0,0,0), en1[2])
        line2 = sp.Line3D((0,0,0), en2[2])
        line3 = sp.Line3D((0,0,0), en3[2])
        #if line1.is_perpendicular(line2) and line2.is_perpendicular(line3) and line1.is_perpendicular(line3):
        #if line1.is_perpendicular(line2) and line2.is_perpendicular(line3):
        if np.cross(line2.p2-line2.p1, line1.p2 - line1.p1).dot(line3.p2 - line3.p1) != 0:
            a = en1[0].distance(en1[1])
            b = en2[0].distance(en2[1])
            c = en3[0].distance(en3[1])
            currentVolume = a*b*c
            #if currentVolume == 125/2:
             #   print 'hop'

            #print 'volume = {0}'.format(currentVolume)

            if currentVolume < minVolume:
                minVolume = currentVolume
                supportingPlanes = (en1[0], en1[1], en2[0], en2[1], en3[0], en3[1])

    return supportingPlanes[0],supportingPlanes[1], supportingPlanes[2], supportingPlanes[3], supportingPlanes[4], supportingPlanes[5]






def addLines(points, edgeDict, normal):
    for p1,p2 in itertools.combinations(points, 2):
        line = sp.Line3D(p1, p2)
        key = '{0},{1}'.format(p1,p2)
        reverseKey = '{0},{1}'.format(p2,p1)

        if key not in edgeDict and reverseKey not in edgeDict:
            edgeDict[key] = [line, normal]
        else:
            if key in edgeDict:
                value = edgeDict[key]
                if len(value)<3:
                    value.append(normal)
                    edgeDict[key] = value
            if reverseKey in edgeDict:
                reverseValue = edgeDict[reverseKey]
                if len(reverseKey)<3:
                    reverseValue.append(normal)
                    edgeDict[reverseKey] = value
