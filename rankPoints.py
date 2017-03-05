from __future__ import division
import scipy.spatial as sci
import numpy as np
import sympy as sp
from plotHelper import plotPoints
from plotHelper import showPlot
from plotHelper import plotConvexHull
from enclosingParallelepiped import findMinimumEnclosingParallelepiped

def buildPetuninEllipses(pointsDict):
    p1,p2,p3,p4,p5,p6 = findMinimumEnclosingParallelepiped(map(lambda x: x[0], pointsDict))
    calculateParallelepipedPointsFromPlanes(p1,p2,p3,p4,p5,p6)

    # verts = findParallelepiped(pointsDict)
    # startPoint = min(verts, key=lambda x: x[0])
    # a = verts[0].distance(verts[1])
    # b = verts[1].distance(verts[2])
    # c = verts[0].distance(verts[4])

    print 'a={0}\nb={1}\nc={2}'.format(a,b,c)

def calculateParallelepipedPointsFromPlanes(leftPlane,rightPlane,upPlane,downPlane,frontPlane,backPlane):
    # temp = frontPlane.intersection(leftPlane)[0]
    # temp2 = downPlane.intersection(temp)
    v1 = downPlane.intersection(frontPlane.intersection(leftPlane)[0])[0]
    v2 = downPlane.intersection(backPlane.intersection(leftPlane)[0])[0]
    v3 = downPlane.intersection(backPlane.intersection(rightPlane)[0])[0]
    v4 = downPlane.intersection(frontPlane.intersection(rightPlane)[0])[0]

    w1 = upPlane.intersection(frontPlane.intersection(leftPlane)[0])[0]
    w2 = upPlane.intersection(backPlane.intersection(leftPlane)[0])[0]
    w3 = upPlane.intersection(backPlane.intersection(rightPlane)[0])[0]
    w4 = upPlane.intersection(frontPlane.intersection(rightPlane)[0])[0]

    plotPoints([v1, v2, v3, v4, w1, w2, w3, w4], 'ro')
    showPlot()
    print 'v1={0}\nv2={1}\nv3={2}\nv4={3}\nw1={4}\nw2={5}\nw3={6}\nw4={7}\n'.format( \
        v1, v2, v3, v4, w1, w2, w3, w4)

    return v1, v2, v3, v4, w1, w2, w3, w4

def calculateParallelepipedPoints(d1,d2, q1, q2, p1, p2):
    diameter = sp.Line3D(d1, d2)
    diamPlane = sp.Plane(d1, d2, q1)
    upPlane = diamPlane.parallel_plane(p1)
    downPlane = diamPlane.parallel_plane(p2)

    diamPerpPlane = diamPlane.perpendicular_plane(d1, d2)
    rightPlane = diamPerpPlane.parallel_plane(q1)
    leftPlane = diamPerpPlane.parallel_plane(q2)
    normal_vector = sp.Point3D(d2[0]-d1[0], d2[1]-d1[1], d2[2]-d1[2])
    backPlane = sp.Plane(d1, normal_vector = normal_vector)
    frontPlane = sp.Plane(d2, normal_vector = normal_vector)

    v1 = downPlane.intersection(frontPlane.intersection(leftPlane)[0])[0]
    v2 = downPlane.intersection(backPlane.intersection(leftPlane)[0])[0]
    v3 = downPlane.intersection(backPlane.intersection(rightPlane)[0])[0]
    v4 = downPlane.intersection(frontPlane.intersection(rightPlane)[0])[0]

    w1 = upPlane.intersection(frontPlane.intersection(leftPlane)[0])[0]
    w2 = upPlane.intersection(backPlane.intersection(leftPlane)[0])[0]
    w3 = upPlane.intersection(backPlane.intersection(rightPlane)[0])[0]
    w4 = upPlane.intersection(frontPlane.intersection(rightPlane)[0])[0]

    plotPoints([v1,v2,v3,v4,w1,w2,w3,w4], 'ro')
    showPlot()
    print 'v1={0}\nv2={1}\nv3={2}\nv4={3}\nw1={4}\nw2={5}\nw3={6}\nw4={7}\n'.format( \
        v1, v2, v3, v4, w1, w2, w3, w4)

    return v1,v2,v3,v4,w1,w2,w3,w4





def findParallelepiped(pointsDic):
    onlyPoints = map(lambda x: x[0], pointsDic)

    convexHull = sci.ConvexHull(onlyPoints)
    print convexHull.vertices
    verts = convexHull.vertices
    plotPoints(map(lambda x: onlyPoints[x], verts))
    #plotPoints(onlyPoints)
    plotConvexHull(onlyPoints, convexHull.simplices, 'k-')


    #find two farthest points
    maxDist = 0
    d1Ind, d2Ind = 0, 0
    tempVerts = verts
    for i in verts:
        tempVerts = [k for k in tempVerts if k != i]
        for j in tempVerts:
            p1 = sp.Point3D(onlyPoints[i])
            p2 = sp.Point3D(onlyPoints[j])
            currentDist = p1.distance(p2)
            if(currentDist > maxDist):
                maxDist = currentDist
                d1Ind, d2Ind = i, j

    d1 = sp.Point3D(onlyPoints[d1Ind])
    d2 = sp.Point3D(onlyPoints[d2Ind])
    # d1Ind = 8545
    # d2Ind = 23600
    # maxDist = 0
    # d1 = sp.Point3D(255, 252, 255)
    # d2 = sp.Point3D(0, 8, 0)
    print 'd1ind={0}; d2Ind={1}'.format(d1Ind, d2Ind)
    print 'p1={0};\np2={1};\nmaxDist={2}'.format(d1, d2, maxDist)

    #find farthest point from d1d2 line
    d1d2 = sp.Line3D(d1, d2) #diameter

    maxDist = 0
    q1Ind = 0
    without_d1d2 = [i for i in verts if i not in (d1Ind, d2Ind)]
    print 'size with d1d2 = {0}\nsize without d1d2 = {1}'.format(len(verts), len(without_d1d2))

    for i in without_d1d2:
        currentPoint = sp.Point3D(onlyPoints[i])
        currentDist = d1d2.distance(currentPoint)
        if currentDist > maxDist:
            maxDist = currentDist
            q1Ind = i

    q1 = sp.Point3D(onlyPoints[q1Ind])
    print 'q1={0}'.format(q1)

    #find two most farthest points from plain that defined by d1 d2 q1  (0, 180, 255) 5817
    d1d2q1 = sp.Plane(d1, d2, q1)
    normal = d1d2q1.normal_vector
    A, B, C = normal[0], normal[1], normal[2]
    D = -A*d1[0] - B*d1[0] - C*d1[2]

    p1Ind = q1Ind   # point from right side plane
    p2Ind = q1Ind   # point from left side plane

    maxDistRight = 0
    maxDistLeft = 0

    for i in [j for j in verts if j not in (d1Ind, d2Ind, q1Ind)]:
        currentPoint = sp.Point3D(onlyPoints[i])
        currentDist = d1d2q1.distance(currentPoint)
        subtitution = currentPoint[0]*A + currentPoint[1]*B + currentPoint[2]*C + D
        if subtitution > 0:
            if currentDist > maxDistRight:
                maxDistRight = currentDist
                p1Ind = i
        else:
            if currentDist > maxDistLeft:
                maxDistLeft = currentDist
                p2Ind = i

    p1 = sp.Point(onlyPoints[p1Ind])
    p2 = sp.Point(onlyPoints[p2Ind])

    print 'p1={0}\np2={1}'.format(p1,p2)

    #find the last point to defind last plane
    q2Ind = d1Ind
    maxDist = 0
    perpend_plane_to_d1d2q1 = d1d2q1.perpendicular_plane(d1, d2)
    normal = perpend_plane_to_d1d2q1.normal_vector
    A, B, C = normal[0], normal[1], normal[2]
    D = -A * d1[0] - B * d1[0] - C * d1[2]
    sign = A * q1[0] + B * q1[1] + C * q1[2] + D
    isRight = False
    if sign > 0:
        isRight = True

    for i in [j for j in verts if j not in (d1Ind, d2Ind, p1Ind, p2Ind, q1Ind)]:
        currentPoint = sp.Point3D(onlyPoints[i])
        currentDist = perpend_plane_to_d1d2q1.distance(currentPoint)
        subtitution = currentPoint[0] * A + currentPoint[1] * B + currentPoint[2] * C + D
        if isRight:
            if subtitution < 0 and currentDist > maxDist:
                maxDist = currentDist
                q2Ind = i
        else:
            if subtitution > 0 and currentDist > maxDist:
                maxDist = currentDist
                q2Ind = i

    q2 = sp.Point3D(onlyPoints[q2Ind])
    print 'q2={0}'.format(q2)

    #plotPoints([d1,d2,q1,q2,p1,p2], 'r')


    ppp = calculateParallelepipedPoints(d1,d2, q1,q2, p1,p2)  #parallelepiped points

    return ppp

















