import cv2
img1 = cv2.imread('clavelR.jpg')
img2 = cv2.imread('clavel.jpg')
img3=img1[1:568,1:1001,:]
dst = cv2.addWeighted(img3,0.3,img2,0.3,0)
cv2.imshow('dst',dst)
cv2.imwrite('dst.png',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
