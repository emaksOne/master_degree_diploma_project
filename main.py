from PIL import Image
from utils import createPointsDictionary
from rankPoints import buildPetuninEllipses

import mock

def main():
    path = 'window.jpg'

    im = Image.open(path)
    pix = im.load()

    width, hight = im.size
    print im.size

    pointsDict = createPointsDictionary(pix, width, hight)
    rankingPoints = buildPetuninEllipses(pointsDict)

# def main():
#
#     #pointsDict = mock.generateTetraeder()
#     #pointsDict = mock.generateRombCube()
#     pointsDict = mock.generatePointDictionaryFake()
#     rankingPoints = buildPetuninEllipses(pointsDict)

main()
