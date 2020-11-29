# Kép invertálása

# NumPy és OpenCV csomagok importálása.
# az OpenCV csomagot ritkán, de szokták "cv" néven importálni (import cv2 as cv). De ez egyáltalán nem olyan gyakori, mint a NumPy esetén az "np" rövidítés, ezért a kódokban nem használom ezt a megoldást.
import cv2
thresh = 128

#read image1
original = cv2.imread('kartya.png', cv2.IMREAD_GRAYSCALE)
img_binary = cv2.threshold(original, thresh, 255, cv2.THRESH_BINARY)[1]

#save image
cv2.imshow("Original",img_binary)
#cv2.imshow("Shape", shape)
#cv2.imshow("2: Invertalt kep okosabban", I_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
