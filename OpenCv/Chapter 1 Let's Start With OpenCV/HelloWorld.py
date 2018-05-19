import cv2.cv as cv
image = cv.LoadImage('ri.jpg',cv.CV_LOAD_IMAGE_COLOR)
font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX,1,1,0,3,8)
y = image.height / 2
x = image.width / 4
cv.PutText(image,"Hello World !",(x,y),font,cv.RGB(255,255,255))
cv.ShowImage('Hello World',image)
cv.WaitKey(0)