import numpy as np
import cv2
 
image = cv2.imread("Input.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 245, 255, cv2.THRESH_BINARY)[1]
kernel = np.ones((5,5), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
contours,hierachy=cv2.findContours(img_dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

s = []
for c in contours:
    s.append(cv2.contourArea(c))
s.sort()

for c in contours:
    for i in range (0,len(contours)):
        if s[i] == cv2.contourArea(c):
            text = len(contours) - i
    if text != 1:
        text = text -1
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        peri=cv2.arcLength(c,True)
        approx=cv2.approxPolyDP(c,0.009*peri,True)
        cv2.drawContours(image,[approx],-1,(0,0,0),2)
        #cv2.putText(image, str(text), (cX, cY),cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)

cv2.imshow("image",image)
cv2.imwrite("Result6.jpg",image)
#cv2.imwrite("Result2.jpg",gray)
#cv2.imwrite("Result3.jpg",blurred)
#cv2.imwrite("Result4.jpg",thresh)
#cv2.imwrite("Result5.jpg",img_dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
print("Coins Number is =", len(contours)-1)
