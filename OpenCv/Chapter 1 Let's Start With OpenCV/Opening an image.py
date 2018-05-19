import cv2.cv as cv
image = cv.LoadImage('ri.jpg',cv.CV_LOAD_IMAGE_COLOR)
cv.NamedWindow('Rishav',cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage('Rishav',image)
cv.WaitKey(0)