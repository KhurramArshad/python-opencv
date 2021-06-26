import cv2 as cv
import numpy as np
"""
creating a blank image(a 2d matrix of zeros having image datatype with 3 color channels)
here uint8 is datatype of an image

"""
blank = np.zeros((500,500,3), dtype='uint8')
#showing a blank image
cv.imshow('Blank image', blank)
# 1. paint the image a certain color
# giving color to whole image
blank[:] = 0,255,0 #BGR
cv.imshow('Green image', blank)
# Giving color to some specifc area or pixels of image
blank[200:300, 300:400] = 0,0,255 #BGR
cv.imshow('Green image', blank)

# 2. Draw a rectangle
# cv.rectangle(blank, (origin point-1), (point-2), (color), thickness=2 )
# cv.rectangle(blank, (origin point-1), (point-2), (color), thickness=cv.FILLED )
# cv.rectangle(blank, (origin point-1), (point-2), (color), thickness=-1 )
# cv.rectangle(blank, (origin point-1), (blank.shape[1]//2, blank.shape[0]//2), (color), thickness=cv.FILLED )
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2) # rectangle from origin to (250,250)
cv.imshow('Rectangle', blank)

# 3. Draw a Circle
#cv.circle(blank, (centre), radius, (color), thickness=3)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

# 4. Draw a Line
#cv.line(blank, (start point), (end point), (color), thickness=5)
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=5)
cv.imshow('Line', blank)

# 5. write text on an image
#cv.putText(blank, 'Text', (where to write), fontStyle, fontScale, color, thickness)
cv.putText(blank, 'Khurram', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)
cv.waitKey(0)