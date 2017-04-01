from __future__ import division
import scipy.spatial as sci
import numpy as np
import sympy as sp
from plotHelper import plotPoints
from plotHelper import showPlot
from plotHelper import plotConvexHull
from enclosingParallelepiped import findMinimumEnclosingParallelepiped
from sys import maxint

def buildPetuninEllipses(pointsDict):
    p1,p2,p3,p4,p5,p6 = findMinimumEnclosingParallelepiped(map(lambda x: x[0], pointsDict))

    q1,q2,q3,q4,q5,q6,q7,q8 = calculateParallelepipedPointsFromPlanes(p1,p2,p3,p4,p5,p6)

    v1,v2,v3 = findCustomBasis(q1,q2,q3,q4,q5,q6,q7,q8)

    customBasis = np.column_stack((v1,v2,v3))
    
    print 'basis = {0}'.format(customBasis)

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
    showPlot()
    print 'v1={0}\nv2={1}\nv3={2}\nv4={3}\nw1={4}\nw2={5}\nw3={6}\nw4={7}\n'.format( \
        v1, v2, v3, v4, w1, w2, w3, w4)

    return v1, v2, v3, v4, w1, w2, w3, w4

def calculateDistance(p1,p2):
    distance = (p2[0]-p1[0])*2 + (p2[1]-p1[1])*2 +(p2[1]-p1[1])*2
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



















