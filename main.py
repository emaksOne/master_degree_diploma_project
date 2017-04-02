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

    for info in rankingPoints:
        rgb = info[0]
        position = info[1]
        mark = info[2]
        if mark:
            rgb = (172, 172, 172)
        pix[position] = rgb
    im.save('filtered.png')


# def main():
#
#     #pointsDict = mock.generateTetraeder()
#     #pointsDict = mock.generateRombCube()
#     pointsDict = mock.generatePointDictionaryFake()
#     rankingPoints = buildPetuninEllipses(pointsDict)

main()
