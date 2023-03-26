import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img1 = cv2.imread(r"G:\University Stuff\8th semester\Dip\Assignment#1-(B)\data\bottle1.jpg",cv2.IMREAD_GRAYSCALE)
img2= cv2.imread(r"G:\University Stuff\8th semester\Dip\Assignment#1-(B)\data\bottle2.jpg",cv2.IMREAD_GRAYSCALE)

ret, size=cv2.threshold(img1, 40, 255, cv2.THRESH_BINARY)

ret, thresh1=cv2.threshold(img1, 190, 255, cv2.THRESH_BINARY)
ret, thresh2=cv2.threshold(img2, 190, 255, cv2.THRESH_BINARY)

# thresh1 = cv2.bitwise_not(thresh1)
# thresh2 = cv2.bitwise_not(thresh2)

total_size = 0
first = 0
second = 0

for rows in size:
    n = cv2.countNonZero(rows)
    total_size += n

for rows in thresh1:
    n = cv2.countNonZero(rows)
    first += n

for rows in thresh2:
    n = cv2.countNonZero(rows)
    second += n

firstPercentage = 100 - ((first/total_size)*100)
secondPercentage = 100-((second/total_size)*100)

print("Percentage of the first bottle: ",firstPercentage,"\n")
print("Percentage of the second bottle: ",secondPercentage)
cv2.imshow("half", thresh1)
cv2.imshow("full", thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()