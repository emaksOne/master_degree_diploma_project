#pointsDict  its {rgb=[r,g,b], pos=[x,y]} collection
import scipy.spatial.distance as sci
import numpy as np

def buildPetuninEllipses(pointsDict):
    d1, d2 = findMostFarestTwoPoints(pointsDict)




def findMostFarestTwoPoints(pointsDict):
    distances = sci.squareform(sci.pdist(pointsDict[0]))
    posd1, posd2 = np.unravel_index(distances.argmax(), distances.shape)
    return pointsDict[posd1, posd2]



