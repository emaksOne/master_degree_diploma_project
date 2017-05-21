from unittest import TestCase
from enclosingParallelepiped import findMinimumEnclosingParallelepiped
from rankPoints import calculateParallelepipedPointsFromPlanes
import mock
import sympy as sp


class TestFindMinimumEnclosingParallelepiped(TestCase):
    def test_findMinimumEnclosingParallelepipedPoints_cube(self):
        #arrange
        v1 = sp.Point3D(0, 5, 5)
        v2 = sp.Point3D(0, 5, 0)
        v3 = sp.Point3D(6, 5, 0)
        v4 = sp.Point3D(6, 5, 5)
        v5 = sp.Point3D(0, 0, 5)
        v6 = sp.Point3D(0, 0, 0)
        v7 = sp.Point3D(6, 0, 0)
        v8 = sp.Point3D(6, 0, 5)
        expectedPoints = [v1, v2, v3, v4, v5, v6, v7, v8]
        pointsDict = mock.generateCube()

        #act
        p1, p2, p3, p4, p5, p6, convexVerts = findMinimumEnclosingParallelepiped(map(lambda x: x[0], pointsDict))
        q1, q2, q3, q4, q5, q6, q7, q8 = calculateParallelepipedPointsFromPlanes(p1, p2, p3, p4, p5, p6)
        actualPoints = [q1, q2, q3, q4, q5, q6, q7, q8]

        #assert
        self.assertItemsEqual(expectedPoints, actualPoints)

    def test_findMinimumEnclosingParallelepipedPoints_tetraeder(self):
        #arrange
        v1 = sp.Point3D(0, 5, 0)
        v2 = sp.Point3D(0, 5, 5)
        v3 = sp.Point3D(5, 5, 5)
        v4 = sp.Point3D(5, 5, 0)
        v5 = sp.Point3D(0, 0, 0)
        v6 = sp.Point3D(0, 0, 5)
        v7 = sp.Point3D(5, 0, 5)
        v8 = sp.Point3D(5, 0, 0)
        expectedPoints = [v1, v2, v3, v4, v5, v6, v7, v8]
        pointsDict = mock.generateTetraeder()

        #act
        p1, p2, p3, p4, p5, p6, convexVerts = findMinimumEnclosingParallelepiped(map(lambda x: x[0], pointsDict))
        q1, q2, q3, q4, q5, q6, q7, q8 = calculateParallelepipedPointsFromPlanes(p1, p2, p3, p4, p5, p6)
        actualPoints = [q1, q2, q3, q4, q5, q6, q7, q8]

        #assert
        self.assertItemsEqual(expectedPoints, actualPoints)

    def test_findMinimumEnclosingParallelepipedPoints_rombCube(self):
        # arrange
        v1 = sp.Point3D(2, 2, 0)
        v2 = sp.Point3D(0, 0, 4)
        v3 = sp.Point3D(-2, 2, 8)
        v4 = sp.Point3D(0, 4, 4)
        v5 = sp.Point3D(6, 2, 0)
        v6 = sp.Point3D(4, 0, 4)
        v7 = sp.Point3D(2, 2, 8)
        v8 = sp.Point3D(4, 4, 4)
        expectedPoints = [v1, v2, v3, v4, v5, v6, v7, v8]
        pointsDict = mock.generateRombCube()

        # act
        p1, p2, p3, p4, p5, p6, convexVerts = findMinimumEnclosingParallelepiped(map(lambda x: x[0], pointsDict))
        q1, q2, q3, q4, q5, q6, q7, q8 = calculateParallelepipedPointsFromPlanes(p1, p2, p3, p4, p5, p6)
        actualPoints = [q1, q2, q3, q4, q5, q6, q7, q8]

        # assert
        self.assertItemsEqual(expectedPoints, actualPoints)

