import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\Moiz\Desktop\dip assignment 1\data\test.png",cv2.IMREAD_UNCHANGED)

#cv2.imshow("Window",img)
print("Old index: ",img[140,115])
#print(img.shape)

for x in range(0,img.shape[0]):
    for y in range(0,img.shape[1]):
        if (img[x][y][0]>=80 and img[x][y][0]<=85 and img[x][y][1]>=80 and img[x][y][1]<=85 and img[x][y][2]>=80 and img[x][y][2]<=85):
                img[x][y][3] = 0
        
#newImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print("Modified index: ",img[140,115])
plt.imshow(img)
plt.show()

# cv2.imshow("Window",img)

# cv2.waitKey(0)

# cv2.destroyAllWindows()