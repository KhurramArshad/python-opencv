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