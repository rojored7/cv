import cv2
import numpy as np
image = cv2.imread('rosasb.jpg')
#cap = cv2.VideoCapture(0)
while(1):
  # Take each frame
  #_, frame = cap.read()
  # Convert BGR to HSV
  hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  # define range of blue color in HSV
  lower_verde = np.array([25,50,50])
  upper_verde = np.array([67,255,255])
  lower_rosa1 = np.array([125,50,50])
  upper_rosa1 = np.array([167,255,255])
  # Threshold the HSV image to get only blue colors
  mask = cv2.inRange(hsv, lower_verde, upper_verde)
  mask1 = cv2.inRange(hsv, lower_rosa1, upper_rosa1)
  # Bitwise-AND mask and original image
  bola = cv2.bitwise_and(image,image, mask= mask)
  camiseta = cv2.bitwise_and(image,image, mask= mask1)
  cv2.imshow('frame',image)
  cv2.imshow('mask',mask)
  cv2.imshow('Bola',bola)
  cv2.imshow('Camiseta',camiseta)
  k = cv2.waitKey(5) &amp; 0xFF
  # si pulsa q se rompe el ciclo
  if k == ord("q"):
    break
cv2.destroyAllWindows()
