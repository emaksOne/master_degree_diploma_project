from __future__ import division
import scipy.spatial as sci
import numpy as np
import sympy as sp
from plotHelper import plotPoints
from plotHelper import plotConvexHull
import itertools
from sys import maxint
from sympy import are_similar

def findMinimumEnclosingParallelepiped(points):
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
        p1 = sp.Point3D(points[face[0]])
        p2 = sp.Point3D(points[face[1]])
        p3 = sp.Point3D(points[face[2]])
        plane = sp.Plane(p1,p2,p3)
        addLines([p1,p2,p3], edgesDict, plane.normal_vector)
        plane = sp.Plane(p1, p2, p3)
        maxDist = 0
        pMaxInd = 0
        for i in verts:
            point = sp.Point3D(points[i])
            currentDist = plane.distance(point)
            if(currentDist > maxDist):
                maxDist = currentDist
                pMaxInd = i

        paralelPlane = plane.parallel_plane(points[pMaxInd])
        if plane.equation() != paralelPlane.equation():
            normal = plane.normal_vector
            entity = (plane, paralelPlane, normal)
            if entity not in N:
                N.append(entity)

    print 'N size = {0}'.format(len(N))
    print 'edges size is {0}'.format(len(edgesDict))
    edges = edgesDict.values()

    def isCorrectEdge(edge1):
        p1 = edge1.p1
        p2 = edge1.p2
        key = '{0},{1}'.format(p1, p2)
        reverseKey = '{0},{1}'.format(p2, p1)
        #observe = []
        value = edgesDict.get(key, None)
        reverseValue = edgesDict.get(reverseKey, None)
        if not value and not reverseValue:
            return False
        if not reverseValue:
            observe = value
        else:
            observe = reverseValue
        direction = p2 - p1
        dot1 = np.dot(direction, observe[1])
        dot2 = np.dot(direction, observe[2])
        if dot1 * dot2 <= 0:
            return True
        return False

    def isCorrect(edge, normal):
        p1 = edge.p1
        p2 = edge.p2
        key = '{0},{1}'.format(p1, p2)
        reverseKey = '{0},{1}'.format(p2, p1)
        # observe = []
        value = edgesDict.get(key, None)
        reverseValue = edgesDict.get(reverseKey, None)
        if not value and not reverseValue:
            return False
        if not reverseValue:
            observe = value
        else:
            observe = reverseValue
        dot1 = np.dot(normal, observe[1])
        dot2 = np.dot(normal, observe[2])
        if dot1 * dot2 < 0:
            return True
        return False


    for i in range(len(edges)):
        #print 'i = {0}'.format(i)
        for j in range(i+1,len(edges)):
            #print 'j = {0}'.format(j)
            e1 = edges[i][0]
            e2 = edges[j][0]
            if not e1.is_parallel(e2):
                if isCorrectEdge(e1) and isCorrectEdge(e2):
                    normal = sp.Point3D(np.cross(e1.p2 - e1.p1, e2.p2 - e2.p1))
                    #if isCorrect(e1, normal) and isCorrect(e2, normal):
                    plane = sp.Plane(e1.p1, normal_vector=normal)
                    paralelPlane = sp.Plane(e2.p1, normal_vector=normal)
                    if plane.equation() != paralelPlane.equation():
                        entity = (plane, paralelPlane, normal)
                        if entity not in N:
                            N.append(entity)

    print 'N size = {0}'.format(len(N))

    minVolume = maxint
    supportingPlanes = ()

    for i in range(len(N)):
        print 'i = {0}'.format(i)
        for j in range(i+1, len(N)):
            print 'j = {0}'.format(j)
            for k in range(j+1, len(N)):
                en1 = N[i]
                en2 = N[j]
                en3 = N[k]
                line1 = sp.Line3D((0,0,0), en1[2])
                line2 = sp.Line3D((0,0,0), en2[2])
                line3 = sp.Line3D((0,0,0), en3[2])
                if line1.is_perpendicular(line2) and line2.is_perpendicular(line3) and line1.is_perpendicular(line3):
                    a = en1[0].distance(en1[1])
                    b = en2[0].distance(en2[1])
                    c = en3[0].distance(en3[1])
                    currentVolume = a*b*c
                    
                    print 'volume = {0}'.format(currentVolume)

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
