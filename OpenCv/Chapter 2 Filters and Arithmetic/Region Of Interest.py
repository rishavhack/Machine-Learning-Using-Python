import cv2.cv as cv
im = cv.LoadImage("t.png",3)
cv.SetImageROI(im,(50,50,150,150))
cv.Zero(im)

cv.ResetImageROI(im)
cv.ShowImage("Image",im)
cv.WaitKey(0)