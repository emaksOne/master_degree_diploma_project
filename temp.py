import numpy
import scipy
from scipy import ndimage
import sys


sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('example.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

im = scipy.misc.imread('13_1.bmp')
im = im.astype('int32')
dx = ndimage.sobel(im, 0)  # horizontal derivative
dy = ndimage.sobel(im, 1)  # vertical derivative
mag = numpy.hypot(dx, dy)  # magnitude
mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)
scipy.misc.imsave('sobel.jpg', mag)


