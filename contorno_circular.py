import cv2
img = cv2.imread('rosasb.jpg',0)
ret,thresh = cv2.threshold(img,0,255,0)
contours, hierarchy = cv2.findContours(thresh,1,2)
cnt = contours[0]
M = cv2.moments(cnt)
print(M)
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img,center,radius,(0,255,0),2)

#epsilon = 0.1 * cv2.arcLength(countours[0], True)
#approx = cv2.approxPolyDP(countours[0], epsilon, True)
#print(approx)
#cv2.imshow('im',approx)
#cv2.drawContours(img, approx, -1, (0, 255, 0), 3)
cv2.imshow("Contour", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
