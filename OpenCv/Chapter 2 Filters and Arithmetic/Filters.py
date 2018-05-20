import cv2.cv as cv
image = cv.LoadImage('t.png',cv.CV_LOAD_IMAGE_COLOR)
cv.ShowImage("Original",image)

grey = cv.CreateImage((image.width,image.height),8,1)
cv.CvtColor(image,grey,cv.CV_RGBA2GRAY)
cv.ShowImage('Greyed',grey)

smoothed = cv.CloneImage(image)
cv.Smooth(image,smoothed,cv.CV_MEDIAN)
cv.ShowImage("Smoothed",smoothed)

cv.EqualizeHist(grey,grey)
cv.ShowImage("Equalized",grey)

threshold1 = cv.CloneImage(grey)
cv.Threshold(threshold1,threshold1,100,255,cv.CV_THRESH_BINARY)
cv.ShowImage("Threshold",threshold1)

threshold2 = cv.CloneImage(grey)
cv.Threshold(threshold2,threshold2,100,255,cv.CV_THRESH_OTSU)
cv.ShowImage("Threshold 2",threshold2)

element_shape = cv.CV_SHAPE_RECT
pos = 3
element = cv.CreateStructuringElementEx(pos*2+1,pos*2+1,pos,pos,element_shape)
cv.Dilate(grey,grey,element,2)

cv.ShowImage("Dilated",grey)

cv.WaitKey(0)