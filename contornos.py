import cv2
img = cv2.imread('ella.jpg',0)
ret,thresh = cv2.threshold(img,50,255,0)
contours, hierarchy = cv2.findContours(thresh,1,2)
cnt = contours[0]
M = cv2.moments(cnt)
print(M)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
area = cv2.contourArea(cnt)
countours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

epsilon = 1000 * cv2.arcLength(countours[0], True)
approx = cv2.approxPolyDP(countours[0], epsilon, True)
print(approx)
#cv2.imshow('im',approx)
cv2.drawContours(img, approx, -1, (0, 255, 0), 3)
cv2.imshow("Contour", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
