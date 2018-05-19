import cv2.cv as cv
im = cv.LoadImage('ri.jpg')
thumb = cv.CreateImage((im.width / 2, im.height /2),8,3)
cv.Resize(im,thumb)
cv.SaveImage("thumb.png",thumb)