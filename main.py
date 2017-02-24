from PIL import Image
from utils import createPointsDictionary
from rankPoints import buildPetuninEllipses
import mock





def main():
    #path = 'images.jpeg'

    #im = Image.open(path)
    #pix = im.load()
    pix = mock.generateTestData()
    #width, hight = im.size
    width, hight = 10,8

    pointsDict = createPointsDictionary(pix, width, hight)
    rankingPoints = buildPetuninEllipses(pointsDict)

main()