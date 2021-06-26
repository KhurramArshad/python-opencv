# python-opencv
Basics of python open cv
OpenCV

Installation:
Pip install opencv-contrib-python
Pip install caer #this package is help ful to do vision part fast
Pip install canaro # this package has built in tensorflow

Reading Images:

import cv2 as cv
# the method imread takes path of image as argument and returns matrix of image pixels
img = cv.imread('img.jpg')
 
"""
the method imshow below displays the image as window,
it takes two arguments first is window name and second
is image
 
"""
cv.imshow('person image', img)
 
"""
waitKey function is keyboard bounding function, for time bound
 
"""
cv.waitKey(0)

Reading Video:

import cv2 as cv
 
"""the method VideoCapture() either takes integer(0,1,2,3,...) or path of video as argument 
and reads the video"""
 
capture = cv.VideoCapture('video.mp4')
 
"""
the method capture.read() below reads the video frame by frame
and returns two things first boolean status whether the frame is read successfully or not,
second is the frame. we use this method in while loop because video can have many frames so 
to read all those frames we use while loop.
 
to show the video in a window we use imshow() method discussed before in image read section
 
"""
while True:
    isTrue, frame = capture.read()
    cv.imshow('my video', frame)
    # for closing the video window (breaking the while loop) we use the following
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
 
 
"""
to release the video frames we use release() method
 
"""
capture.release()
cv.destroyAllWindows()
 


Resizing and Rescaling:

Method-1:
import cv2 as cv
"""
for resizing we are making one seperate function named rescaleFrame(),
it takes two arguments first is frame and second is scale
and returns resized frame
"""
def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
 
"""the method VideoCapture() either takes integer(0,1,2,3,...) or path of video as argument 
and reads the video"""
 
capture = cv.VideoCapture('video.mp4')
 
"""
the method capture.read() below reads the video frame by frame
and returns two things first boolean status whether the frame is read successfully or not,
second is the frame. we use this method in while loop because video can have many frames so 
to read all those frames we use while loop.
 
to show the video in a window we use imshow() method discussed before in image read section
 
"""
while True:
    isTrue, frame = capture.read()
    # calling rescaleFram() function
    frame_resized = rescaleFrame(frame)
    cv.imshow('my video', frame)
    cv.imshow('my resized video', frame_resized)
    # for closing the video window (breaking the while loop) we use the following
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
 
 
"""
to release the video frames we use release() method
 
"""
capture.release()
cv.destroyAllWindows()
 


Method-2:
import cv2 as cv
"""
for resizing we are making one seperate function named changeRes(),
this method is only used for live videos like web cam or external IP cams 
not for images or recorded videos
it takes two arguments first is width in pixels and second is height pixels
 
"""
def changeRes(width, height):
    # here property 3 relates to width
    capture.set(3,width)
    # here property 4 relates to height
    capture.set(4,width)
 
"""the method VideoCapture() either takes integer(0,1,2,3,...) or path of video as argument 
and reads the video"""
 
capture = cv.VideoCapture(0)
# calling changeRes() function
changeRes(1280,720)
"""
the method capture.read() below reads the video frame by frame
and returns two things first boolean status whether the frame is read successfully or not,
second is the frame. we use this method in while loop because video can have many frames so 
to read all those frames we use while loop.
 
to show the video in a window we use imshow() method discussed before in image read section
 
"""
while True:
    isTrue, frame = capture.read()    
    cv.imshow('my video', frame)   
    # for closing the video window (breaking the while loop) we use the following
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
 
 
"""
to release the video frames we use release() method
 
"""
capture.release()
cv.destroyAllWindows()
 


Draw Shapes and Put Text:
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

Essential Functions in OpenCV:

import cv2 as cv
 
img = cv.imread('img1.jpg')
cv.imshow('MyImage', img)
 
# Converting image to GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
 
# Blur an image
#cv.GaussianBlur(img, (KernalSize), Border)
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
 
# Finding Edges in an image
canny = cv.Canny(img, 125, 175) # 125,175 are thresh hold values
cv.imshow('Canny', canny)
 
# Dilating an image
dilated = cv.dilate(canny, (7,7), iterations=3) #(7,7) is kernal size
cv.imshow('Dilated', dilated)
 
# Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)
 
# Resize an image
#cv.INTER_CUBIC if enlarging the small image to get batter quality
#cv.INTER_AREA if making size small of the big image to get batter quality
resized = cv.resize(img, (400,400), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)
 
# Cropping
cropped = img[10:10, 20:20]
cv.imshow('Cropped', cropped)
 
cv.waitKey(0)


Face Detection with HaarCasCade:

import cv2 as cv
 
img = cv.imread('img1.jpg')
cv.imshow('MyImage', img)
 
# converting into gray image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('MyImage', gray)
 
#loading haar cascade file
haar_cascade = cv.CascadeClassifier('frontal_face.xml')
 
# detecting faces
# faces_rect contains list of coordinates of faces and to view coord. we can loop over the list
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
print(f'Number of faces found = {len(faces_rect)}')
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
 
cv.imshow('Detected Face', img)
 
 
 
cv.waitKey(0)

Face Recognition Using Deep Learning:






	
