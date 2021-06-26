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
