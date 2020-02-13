import cv2
import sys
from playsound import playsound
from gtts import gTTS
import os
import winsound
from pygame import mixer
mixer.init()
mixer.music.load("good.mp3")

# tts = gTTS(text='Hey! you, Let me tell you something, that might be usefull for you, come here!', lang='en')
# tts.save("good.mp3")
# playsound('good.mp3')
#img=cv.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)

img_counter = 0 
    

  
# font 
font = cv2.FONT_HERSHEY_SIMPLEX 
  
# org 
org = (50, 50) 
  
# fontScale 
fontScale = 1
   
# Blue color in BGR 
color = (255, 0, 0) 
  
# Line thickness of 2 px 
thickness = 2

x = 1
y = 1
w = 1
h = 1
x1 = 1
y1 = 1
x1 = 1
y1 = 1 
count = 0
play = 0
facewasdetected = 0
personwashere = 0
toldhim1=0
toldhim=0
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    k = cv2.waitKey(1)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    cv2.rectangle(frame, (0,0), (1280, 720), (1, 0, 0), -2)
    cv2.circle(frame, (320,360), 180, (255, 255, 255), thickness=-1, lineType=8, shift=0)
    cv2.circle(frame, (960,360), 180, (255, 255, 255), thickness=-1, lineType=8, shift=0)
    
    if(len(faces)>0) :
        x = faces[0][0]
        y = faces[0][1]
        w = faces[0][2]
        h = faces[0][3]
        x1 = x + int(w/2)
        y1 = y + int(h/2)
        x1 = int((x1 - 640)/3)
        y1 = int((y1 - 360)/3)
        count = 1
        facewasdetected = 1
        personwashere = 1
    else: 
        facewasdetected = 0
    
        


    if(count > 0 and play <2 and toldhim1==0):
        # winsound.PlaySound('good.mp3', winsound.SND_ASYNC | winsound.SND_ALIAS )
        playsound('good.mp3', False)
        # playsound.playsound('good.mp3', False)
        # mixer.music.stop()
        # mixer.music.play()
        play = 100
        toldhim1=1
        toldhim =0
        cv2.putText(frame,'I am playing' , org, font,fontScale, color, thickness, cv2.LINE_AA)
    if(count==0 and facewasdetected==0 and personwashere == 1 and play <2):
        playsound('die.mp3', False)
        play = 120
        personwashere = 0
        toldhim =0
        toldhim1 =0
    
    if(play>0):
        play=play-1
        if(play<5):
            if(facewasdetected != 1):
                count=0
                toldhim1=0
            if(facewasdetected==1 and toldhim ==0):
                playsound('close.mp3', False)
                play = 100
                toldhim =1

        

    cv2.circle(frame, (320 - x1,360 + y1), 30, (0, 0, 0), thickness=-1, lineType=8, shift=0)
    cv2.circle(frame, (960 - x1,360 + y1), 30, (0, 0, 0), thickness=-1, lineType=8, shift=0)

    
    
    #Draw a rectangle around the faces
    #for (x, y, w, h) in faces:
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # cv2.putText(frame,'Face I See'+ str(x)+'ccc' + str(y), org, font,fontScale, color, thickness, cv2.LINE_AA) 
        # cv2.circle(frame, (320,360), 3, (0, 255, 0), thickness=-1, lineType=8, shift=0)
        # cv2.circle(frame, (960,360), 3, (0, 255, 0), thickness=-1, lineType=8, shift=0)

    # Display the resulting frame
    cv2.namedWindow('FaceDetection', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('FaceDetection',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow('FaceDetection', frame)

    if k%256 == 27: #ESC Pressed
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "facedetect_webcam_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()