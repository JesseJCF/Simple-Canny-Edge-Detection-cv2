import cv2

img = cv2.imread("trial.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Canny Edge Detection")

def nothing(x):
    pass

# Trackbars
cv2.createTrackbar("Lower Threshold", "Canny Edge Detection", 50, 500, nothing)
cv2.createTrackbar("Upper Threshold", "Canny Edge Detection", 150, 500, nothing)
cv2.createTrackbar("Blur Sigma x10", "Canny Edge Detection", 5, 50, nothing)

while True:
    lower = cv2.getTrackbarPos("Lower Threshold", "Canny Edge Detection")
    upper = cv2.getTrackbarPos("Upper Threshold", "Canny Edge Detection")
    sigma_slider = cv2.getTrackbarPos("Blur Sigma x10", "Canny Edge Detection")

    if upper < lower:
        upper = lower

    sigma = max(sigma_slider / 10.0, 0.1)

    blur = cv2.GaussianBlur(gray, (0, 0), sigmaX=sigma, sigmaY=sigma)
    edges = cv2.Canny(blur, threshold1=lower, threshold2=upper)

    # We need to convert to BGR so the text is visible
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Overlay text
    cv2.putText(
        edges_bgr,
        f"Lower: {lower}  Upper: {upper}  Sigma: {sigma:.2f}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2,
        cv2.LINE_AA
    )

    cv2.imshow("Canny Edge Detection", edges_bgr)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
