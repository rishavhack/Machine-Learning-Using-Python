
# coding: utf-8

# In[1]:


import cv2
import pyautogui


# In[2]:


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');


# In[3]:


eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml');
def mouseMove(x,y):
    pyautogui.moveTo(x,y, duration = 0.5)


# In[4]:


def detect(gray,frame):
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    for (x,y,w,h) in faces:
        pyautogui.moveTo(x,y, duration = 0.5)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1,3)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    return frame


# In[5]:


video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()

