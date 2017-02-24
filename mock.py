import numpy as np

def generateTestData():
    return [[(i+1, 2*i, 3*i) for i in range(10)] for y in range(8)]

data = generateTestData()

print np.array(data)