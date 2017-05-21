from PIL import Image
from utils import createPointsDictionary
from rankPoints import buildPetuninEllipses
from plotHelper import showPlot
import datetime

def processImage(imgPath, targetColor, deltaParams, isBinarization, isFarthestPointOrientation=True, preconditions=None):
    startTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print 'started at {0}'.format(startTime)

    chanks = imgPath.replace('/', '.').split('.')
    if isBinarization:
        targetColor = (0, 0, 0)
        whiteColor = (255, 255, 255)

        targetImgPath = '{0}/results/{1}_binarized.png'.format(chanks[0], chanks[1])
    else:
        targetImgPath = '{0}/results/{1}_filtered.png'.format(chanks[0], chanks[1])

    im = Image.open(imgPath)
    pix = im.load()

    width, hight = im.size
    print 'image size is {0}'.format(im.size)

    pointsDict = createPointsDictionary(pix, width, hight)
    rankingPoints = buildPetuninEllipses(pointsDict, deltaParams, isFarthestPointOrientation, preconditions)

    im.convert("RGBA")

    for info in rankingPoints:
        rgb = info[0]
        position = info[1]
        rgb = (int(rgb[0]), int(rgb[1]), int(rgb[2]))
        mark = info[2]
        if mark:
            rgb = targetColor
        elif isBinarization:
            rgb = whiteColor

        pix[position[0], position[1]] = rgb
    im.save(targetImgPath)

    endTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print 'ended at {0}'.format(endTime)

    fmt = '%Y-%m-%d %H:%M:%S'
    tdelta = datetime.datetime.strptime(endTime, fmt) - datetime.datetime.strptime(startTime, fmt)
    print 'executing time is'
    print tdelta

    showPlot()
