import numpy as np
import cv2
import math
import matplotlib.pyplot as plt
from pylab import *


img_color = cv2.imread( 'img3.bmp', cv2.COLOR_BGR2RGB )
img_hsv = cv2.cvtColor( img_color, cv2.COLOR_BGR2HSV )
jpgheight, jpgwidth, jpgchannel = img_color.shape
img_h, img_s, img_v = cv2.split(img_hsv)
print img_color.shape



fig = figure(0, figsize=(8,8))
ax = fig.add_axes([0.1,0.1,0.8,0.8],polar=1)
n=jpgheight*jpgwidth
radii = np.ones(n)
ww = np.ones(n)*0.02

#print img_h

theta = (img_h/255.)*(2*np.pi)  #np.arange(0.0, 2*np.pi, 2*np.pi/n)

#print theta

bars = ax.bar(theta.flatten(), radii, width=ww, bottom=0.0)



for r,bar in zip(theta.flatten(), bars):
    bar.set_facecolor( cm.hsv( r/(2*np.pi) ))
    bar.set_alpha(1)


show()





