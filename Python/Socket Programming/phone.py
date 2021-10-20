# importing libraries
import cv2
import numpy as np

cap = cv2.VideoCapture('opencv.mp4')

while(cap.isOpened()):
	ret, frame = cap.read()
  	
  	print(ret)
  	

cap.release()
cv2.destroyAllWindows()