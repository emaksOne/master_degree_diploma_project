from __future__ import division
import scipy.spatial as sci
import numpy as np
import sympy as sp
from plotHelper import plotConvexHull
from plotHelper import plotPoints
from plotHelper import showPlot
from math import fabs
from plotHelper import plotConvexHull
from enclosingParallelepiped import findMinimumEnclosingParallelepiped
from sys import maxint

def buildPetuninEllipses(pointsDict):
    # p1,p2,p3,p4,p5,p6, convexVerts = findMinimumEnclosingParallelepiped(map(lambda x: x[0], pointsDict))
    # print 'convex verts is {0}'.format(convexVerts)
    # q1,q2,q3,q4,q5,q6,q7,q8 = calculateParallelepipedPointsFromPlanes(p1,p2,p3,p4,p5,p6)

    convexVerts = [129,  6816,  12170 , 12485,  12800,  12801,  14381,  15323,  15637,  15952,
        20863,  40512,  43279,  47375,  50543 , 50847 , 50858,  51799,  52112 , 52426,
        52428,  52429 , 52743 , 52744,  53048,  53056,  53057,  53059,  53937,  55260,
        55261,  55268 , 55332 , 55583,  58411,  59048,  59678,  59993,  60304,  60308,
        62206 , 62520 , 62521 , 62522,  63151,  63467,  63781,  65881,  67334,  68403,
        70638  ,75691 , 80100 , 80383,  83473,  85258,  85484,  93649, 100218, 100327,
        100533 ,104628 ,104884 ,111103, 149637, 151215, 151530, 161005, 166261, 167430,
        178692 ,186671]

    q1 = sp.Point3D(131176609 / 1085391, 296726545 / 2170782, 255)
    q2 = sp.Point3D(284089159 / 1085391, 254309825 / 1085391, 255)
    q3 = sp.Point3D(30365715 / 120599, 38866219 / 120599, 255)
    q4 = sp.Point3D(40126295 / 361797, 162566279 / 723594, 255)
    q5 = sp.Point3D(-49855796 / 1085391, -68665570 / 1085391, 0)
    q6 = sp.Point3D(103056754 / 1085391, 74561965 / 2170782, 0)
    q7 = sp.Point3D(30753010 / 361797, 88511419 / 723594, 0)
    q8 = sp.Point3D(-6739280 / 120599, 2980064 / 120599, 0)

    v1,v2,v3 = findCustomBasis(q1,q2,q3,q4,q5,q6,q7,q8)


    transrormationMatrix = np.column_stack((v1,v2,v3))
    transrormationMatrix = (1/255)*transrormationMatrix
    transrormationMatrixInv = np.linalg.inv(transrormationMatrix)

    convexHullInNewBasis = []
    for p in [q1, q2, q3, q4, q5, q6, q7, q8]:
        convexHullInNewBasis.append(np.dot(transrormationMatrixInv, p))

    print convexHullInNewBasis

    center = calculateCenter(convexHullInNewBasis)
    plotPoints([center], 'ro')

    plotPoints(convexHullInNewBasis, 'bo')

    pointsDictNew = applyMatrixToPoints(pointsDict, transrormationMatrixInv, center)

    #pointsDictNewWithRadious = findRadious(pointsDictNew, center)

    pointsDictNew.sort(key=lambda x: x[2], reverse=True)
    pointsDictNewMarked = markPart(pointsDictNew, 10)

    resultedPointsInfo = applyMatrixToPointsBack(pointsDictNewMarked, transrormationMatrix)

    return

    plotPoints(map(lambda x:pointsDictNew[x][0], convexVerts), 'go')

    showPlot()

    #print 'basis = {0}'.format(customBasis)

def calculateParallelepipedPointsFromPlanes(leftPlane,rightPlane,upPlane,downPlane,frontPlane,backPlane):

    v1 = downPlane.intersection(frontPlane.intersection(leftPlane)[0])[0]
    v2 = downPlane.intersection(backPlane.intersection(leftPlane)[0])[0]
    v3 = downPlane.intersection(backPlane.intersection(rightPlane)[0])[0]
    v4 = downPlane.intersection(frontPlane.intersection(rightPlane)[0])[0]

    w1 = upPlane.intersection(frontPlane.intersection(leftPlane)[0])[0]
    w2 = upPlane.intersection(backPlane.intersection(leftPlane)[0])[0]
    w3 = upPlane.intersection(backPlane.intersection(rightPlane)[0])[0]
    w4 = upPlane.intersection(frontPlane.intersection(rightPlane)[0])[0]

    print 'v1={0}\nv2={1}\nv3={2}\nv4={3}\nw1={4}\nw2={5}\nw3={6}\nw4={7}\n'.format( \
        v1, v2, v3, v4, w1, w2, w3, w4)
    plotPoints([v1, v2, v3, v4, w1, w2, w3, w4], 'ro')
    #showPlot()
    print 'v1={0}\nv2={1}\nv3={2}\nv4={3}\nw1={4}\nw2={5}\nw3={6}\nw4={7}\n'.format( \
        v1, v2, v3, v4, w1, w2, w3, w4)

    return v1, v2, v3, v4, w1, w2, w3, w4

def calculateDistance(p1,p2):
    distance = (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 +(p2[2]-p1[2])**2
    return distance ** 0.5

def findCustomBasis(q1,q2,q3,q4,q5,q6,q7,q8):
    # points = [q1,q2,q3,q4,q5,q6]
    # origin = (0,0,0)
    # dist = maxint
    # closerPoint = q1
    # for p in points:
    #     currentDist = calculateDistance(origin, p)
    #     if currentDist < dist:
    #         dist = currentDist
    #         closerPoint = p

    return (q2 - q1, q4 - q1, q5 - q1)

def applyMatrixToPoints(pointInfos, matrix, center):
    newPointsInfos = []
    i = 0
    for info in pointInfos:
        i+=1
        print i
        point = info[0]
        point = np.dot(matrix, point)
        radious = calculateDistance(center, point)
        newPointsInfos.append((point, info[1], radious))

    return newPointsInfos

def applyMatrixToPointsBack(pointInfos, matrix):
    newPointsInfos = []
    i = 0
    for info in pointInfos:
        i += 1
        print i
        point = info[0]
        point = np.dot(matrix, point)
        newPointsInfos.append((point, info[1], info[3]))

    return newPointsInfos

def calculateCenter(points):
    x = (points[1][0] + points[0][0])/2
    y = (points[2][1] + points[1][1])/2
    z = (points[4][2] + points[3][2])/2
    return (x,y,z)

def findRadious(pointInfos, center):
    newPointsInfo = []
    for info in pointInfos:
        point = info[0]
        radious = calculateDistance(center, point)
        newPointsInfo.append((info[0], info[1], radious))

    return newPointsInfo

def markPart(pointsInfo, percent):
    marked = []
    pivot = len(pointsInfo) * (percent/100)
    for index, info in enumerate(pointsInfo):
        mark = False
        if(index < pivot):
            marked = True

        marked.append((info[0], info[1], info[2], mark))

    return marked

















