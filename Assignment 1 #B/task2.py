import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"G:\University Stuff\8th semester\Dip\Assignment#1-(B)\data\brain.tif",cv2.IMREAD_GRAYSCALE)
ret, thresh=cv2.threshold(img, 250, 255, cv2.THRESH_BINARY)
row_pixels=[]
col_pixels=[]

for rows in thresh:
    number = cv2.countNonZero(rows)
    row_pixels.append(number)

transpose = np.transpose(thresh)

for rows in transpose:
    number = cv2.countNonZero(rows)
    col_pixels.append(number)

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10,5))
ax1.set_title('Number of white pixels per row')
ax1.plot(row_pixels)
ax2.set_title('Number of white pixels per column')
ax2.plot(col_pixels)
plt.show()

cv2.imshow("Highlited image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()