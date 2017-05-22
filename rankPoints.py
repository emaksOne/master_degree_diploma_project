from __future__ import division
import numpy as np
from plotHelper import plotPoints
from enclosingParallelepiped import findMinimumEnclosingParallelepiped

def buildPetuninEllipses(pointsDict, deltaParams, isFarthestPointOrientation=True, preconditions=None):
    if preconditions == None:
        p1,p2,p3,p4,p5,p6, convexVerts = findMinimumEnclosingParallelepiped(map(lambda x: x[0], pointsDict))
        print 'convex verts is {0}'.format(convexVerts)
        q1,q2,q3,q4,q5,q6,q7,q8 = calculateParallelepipedPointsFromPlanes(p1,p2,p3,p4,p5,p6)

    else:
        convexVerts = preconditions['convexVerts']
        q1 = preconditions['parallelepipedPoints'][0]
        q2 = preconditions['parallelepipedPoints'][1]
        q3 = preconditions['parallelepipedPoints'][2]
        q4 = preconditions['parallelepipedPoints'][3]
        q5 = preconditions['parallelepipedPoints'][4]
        q6 = preconditions['parallelepipedPoints'][5]
        q7 = preconditions['parallelepipedPoints'][6]
        q8 = preconditions['parallelepipedPoints'][7]

    v1,v2,v3 = findCustomBasis(q1,q2,q3,q4,q5,q6,q7,q8)

    transrormationMatrix = np.column_stack((v1,v2,v3))
    transrormationMatrix = (1/255)*transrormationMatrix
    transrormationMatrixInv = np.linalg.inv(transrormationMatrix)

    convexHullInNewBasis = []
    for p in [q1, q2, q3, q4, q5, q6, q7, q8]:
        convexHullInNewBasis.append(np.dot(transrormationMatrixInv, p))

    center = calculateCenter(convexHullInNewBasis)
    plotPoints([center], 'ro')

    plotPoints(convexHullInNewBasis, 'bo')

    pointsDictNew = applyMatrixToPoints(pointsDict, transrormationMatrixInv, center)

    pointsDictNew.sort(key=lambda x: x[2], reverse=True)
    pointsDictNewMarked = markPart(pointsDictNew, transrormationMatrix, deltaParams, isFarthestPointOrientation)

    resultedPointsInfo = applyMatrixToPointsBack(pointsDictNewMarked, transrormationMatrix)


    plotPoints(map(lambda x:pointsDictNew[x][0], convexVerts), 'go')

    #showPlot()

    return resultedPointsInfo

def calculateParallelepipedPointsFromPlanes(leftPlane,rightPlane,upPlane,downPlane,frontPlane,backPlane):

    v1 = downPlane.intersection(frontPlane.intersection(leftPlane)[0])[0]
    v2 = downPlane.intersection(backPlane.intersection(leftPlane)[0])[0]
    v3 = downPlane.intersection(backPlane.intersection(rightPlane)[0])[0]
    v4 = downPlane.intersection(frontPlane.intersection(rightPlane)[0])[0]

    w1 = upPlane.intersection(frontPlane.intersection(leftPlane)[0])[0]
    w2 = upPlane.intersection(backPlane.intersection(leftPlane)[0])[0]
    w3 = upPlane.intersection(backPlane.intersection(rightPlane)[0])[0]
    w4 = upPlane.intersection(frontPlane.intersection(rightPlane)[0])[0]

    plotPoints([v1, v2, v3, v4, w1, w2, w3, w4], 'ro')
    #showPlot()
    print '\nparallelepiped points is:'
    print 'q1 = sp.{0}\nq2 = sp.{1}\nq3 = sp.{2}\nq4 = sp.{3}\nq5 = sp.{4}\nq6 = sp.{5}\nq7 = sp.{6}\nq8 = sp.{7}\n'.format( \
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
        #print i
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
        #print i
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

def markPart(pointsInfo, matrix, deltaParams, isFarthestPointOrientation):
    marked = []
    farthestPoint = pointsInfo[0][0]
    farthestPoint = np.dot(matrix, farthestPoint)
    nearestPoint = pointsInfo[len(pointsInfo)-1][0]
    nearestPoint = np.dot(matrix, nearestPoint)
    print 'farthest point is {0}'.format(farthestPoint)
    print 'nearest point is {0}'.format(nearestPoint)

    if isFarthestPointOrientation:
        minR = farthestPoint[0]-deltaParams['minR']
        maxR = farthestPoint[0]+deltaParams['maxR']
        minG = farthestPoint[1]-deltaParams['minG']
        maxG = farthestPoint[1]+deltaParams['maxG']
        # minB = farthestPoint[2]+deltaParams['minB']
        # maxB = farthestPoint[2]+deltaParams['maxB']
    else:
        minR = nearestPoint[0] - deltaParams['minR']
        maxR = nearestPoint[0] + deltaParams['maxR']
        minG = nearestPoint[1] - deltaParams['minG']
        maxG = nearestPoint[1] + deltaParams['maxG']
        # minB = nearestPoint[2]+deltaParams['minB']
        # maxB = nearestPoint[2]+deltaParams['maxB']

    for index, info in enumerate(pointsInfo):
        rgb = info[0]
        mark = False
        rgb = np.dot(matrix, rgb)
        r = rgb[0]
        g = rgb[1]
        if r > minR and r < maxR and g > minG and g < maxG:
            # print 'r = {0}, g = {1}, b = {2}'.format(rgb[0], rgb[1], rgb[2])
            mark = True

        marked.append((info[0], info[1], info[2], mark))

    return marked

















