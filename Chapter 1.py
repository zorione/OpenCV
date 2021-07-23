# import cv2
# import numpy as np
# print("Read images, videos & Webcam")
#
# img = cv2.imread("Resources/lena.png")     # import image
# cv2.imshow("Output", img)            #display image
# cv2.waitKey(0)                  #time in miliseconds, 0 means infinite
#
# # cap = cv2.VideoCapture("Resources/test_video.mp4")
# cap = cv2.VideoCapture(0)     #to open webcam
# cap.set(3, 640)
# cap.set(4, 480)
# cap.set(10, 100)      #set brightness
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):         #add delay and looks for key q to break outof loop
#         break




######################################################
import cv2
frameWidth = 640
frameHeigth = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeigth)
cap.set(10, 130)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # add delay and looks for key q to break outof loop
        break
