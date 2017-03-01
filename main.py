from PIL import Image
from utils import createPointsDictionary
from rankPoints import buildPetuninEllipses
import mock



# def main():
#     path = 'images.jpeg'
#
#     im = Image.open(path)
#     pix = im.load()
#
#     width, hight = im.size
#
#     pointsDict = createPointsDictionary(pix, width, hight)
#     rankingPoints = buildPetuninEllipses(pointsDict)

def main():

    pointsDict = mock.generatePointDictionaryFake()
    rankingPoints = buildPetuninEllipses(pointsDict)

main()
