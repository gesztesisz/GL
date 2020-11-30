import numpy as np
import cv2

I = cv2.imread("proba.png")
I = cv2.cvtColor(I.astype(np.uint8), cv2.COLOR_BGR2GRAY)

T = cv2.imread("proba2.png")#.astype(int)
T = cv2.cvtColor(T.astype(np.uint8), cv2.COLOR_BGR2GRAY)

sz = I.shape[1]
m = I.shape[0]

szt = T.shape[1]
mt = T.shape[0]

M0 = np.zeros((m, sz))

for i in range(sz - szt):
    for j in range(m - mt):
        I_roi = I[j:j+mt, i:i+szt].astype(int)
        d = np.sum(np.abs(I_roi - T))
        M0[j, i] = d

(_, _, minloc, _) = cv2.minMaxLoc(M0[:m - mt, :sz - szt])

M0 = ((M0 - M0.min()) / (M0.max() - M0.min()) * 255)#.astype(np.uint8)

M1 = cv2.matchTemplate(I, T.astype(np.uint8), cv2.TM_CCOEFF)

(_, _, _, maxloc) = cv2.minMaxLoc(M1)


cv2.circle(I, (minloc[0] + T.shape[1] // 2, minloc[1] + T.shape[0] // 2), 30, (0, 0, 255), 3)
cv2.circle(I, (maxloc[0] + T.shape[1] // 2, maxloc[1] + T.shape[0] // 2), 20, (0, 255, 0), 3)


cv2.imshow("Waldo", I)
cv2.waitKey(0)
cv2.destroyAllWindows()
