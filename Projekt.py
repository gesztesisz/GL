import cv2
thresh = 128

#read image1
original = cv2.imread("kartya.png")
szurke1= cv2.imread("kartya.png" , cv2.IMREAD_GRAYSCALE)
szurke2 = cv2.threshold(szurke1, thresh, 255, cv2.THRESH_BINARY)[1]


cv2.imshow("Szurkearnyalat",szurke2)
#cv2.imshow("Original2",original)
cv2.imshow("Eredeti",original)

cv2.waitKey(0)
cv2.destroyAllWindows()
