# -*- coding: utf-8 -*-

import numpy as np
import cv2
import pylab as plt
from pylab import rcParams
from matplotlib.patches import Rectangle


node_cascade = cv2.CascadeClassifier('test0/cascade.xml')
rcParams['figure.figsize'] = 12, 8
img = cv2.imread('data/path-of-image.jpg')
resized_image = cv2.resize(img, (640, 480))

plt.imshow(resized_image)
currentAxis = plt.gca()

xx,yy = [],[]
nodes = node_cascade.detectMultiScale(resized_image)
for (x,y,w,h) in nodes:
	xx += [x+w/2.]
	yy += [y+h/2.]
	print ((x,y),(x+w,y+h))
	coords = (x, y), w, h
	currentAxis.add_patch(Rectangle(*coords, fill=True, alpha=0.2, color='#00FF00', edgecolor='#00FF00', linewidth=3))

plt.scatter(xx,yy, color="r")
plt.savefig('temp.jpg')
plt.show()
print "Nb positif :" + str(len(nodes))