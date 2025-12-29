import cv2

img = cv2.imread("trial.png")

# view image using OpenCV
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ------ canny edge detection + vis ------
# the GaussianBlur arguments are: object, kernel size, sigma. 
# with 0.0 sigma, cv2 calculates kernel size
blur = cv2.GaussianBlur(img, (0,0), 2.6) # we could also see about grayscaling first...
canny = cv2.Canny(blur, threshold1=50, threshold2=110)

cv2.imshow("Canny edge detection", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

# saving the canny edge detection result
cv2.imwrite("Canny_Edge_Detection_Result.png", canny)


# i still need to experiment with dilation and erosion to see how they affect the edges