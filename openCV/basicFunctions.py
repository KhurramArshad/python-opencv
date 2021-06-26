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

# Croping
cropped = img[10:10, 20:20]
cv.imshow('Cropped', cropped)

cv.waitKey(0)