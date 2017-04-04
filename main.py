from PIL import Image
from utils import createPointsDictionary
from rankPoints import buildPetuninEllipses
from plotHelper import showPlot

import mock

def main():
    path = 'window.jpg'

    im = Image.open(path)
    pix = im.load()

    pix[0,0] = (172,172,172)

    width, hight = im.size
    print im.size

    pointsDict = createPointsDictionary(pix, width, hight)
    rankingPoints = buildPetuninEllipses(pointsDict)

    i=0
    for info in rankingPoints:
        print i
        i+=1
        rgb = info[0]
        position = info[1]
        rgb = (int(rgb[0]), int(rgb[1]), int(rgb[2]))
        mark = info[2]
        if mark:
            rgb = (172, 172, 172)
        pix[position[0],position[1]] = rgb
    im.save('filtered.png')

    showPlot()


# def main():
#
#     #pointsDict = mock.generateTetraeder()
#     #pointsDict = mock.generateRombCube()
#     pointsDict = mock.generatePointDictionaryFake()
#     rankingPoints = buildPetuninEllipses(pointsDict)

main()
