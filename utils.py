def createPointsDictionary(points, width, hight):
    pointsDict = []
    for x in range(width):
        for y in range(width):
            item = (points[x, y], [x, y])
            pointsDict.append(item)
    return pointsDict