import cv2.cv as cv
im = cv.LoadImage('ri.jpg',cv.CV_LOAD_IMAGE_COLOR)
res= cv.CreateImage(cv.GetSize(im),cv.CV_8UC2,3)
cv.Convert(im,res),cv.ShowImage("Converted",res)
res2=cv.CreateImage(cv.GetSize(im),cv.CV_8UC2,3)
cv.CvtColor(im,res2,cv.CV_RGB2BGR)
cv.ShowImage('CvtColor',res2)
cv.WaitKey(0)