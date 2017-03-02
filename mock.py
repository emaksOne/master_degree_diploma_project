import numpy as np

def generateTestData():
    return [[(i+1, 2*i, 3*i) for i in range(10)] for y in range(8)]

def generatePointDictionaryFake():
    p1 = ((0,0,0), (0,0))
    p2 = ((5,0,0), (0,1))
    p3 = ((5,5,0), (1,0))
    p4 = ((0,5,0), (1,1))

    q1 = ((0, 0, 5), (2, 0))
    q2 = ((5, 0, 5), (2, 1))
    q3 = ((5, 5, 5), (3, 0))
    q4 = ((0, 5, 5), (3, 1))

    b1 = ((2,2,2), (4,0))
    b2 = ((3,3,3), (4,1))
    return [p1,p2,p3,p4,q1,q2,q3,q4,b1,b2]

#data = generateTestData()

#print np.array(data)