import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread(r"G:\University Stuff\8th semester\Dip\Assignment#1-(B)\data\grain.tif",cv2.IMREAD_GRAYSCALE)
def count():

    intensityCount = [0] * 256

    rows = img.shape[0]
    cols = img.shape[1]
    
    for i in range(0,rows):
        for j in range(0,cols):
            imageIntensity=img[i,j]
            intensityCount[imageIntensity]+=1
    
    return intensityCount

def filtering():
    box3x3 = cv2.boxFilter(img, -1, (3,3))
    box7x7 = cv2.boxFilter(img, -1, (7,7))
    #difference = cv2.subtract(box7x7,box3x3)

    # Find the absolute value of the image
    #absoluteImg = cv2.convertScaleAbs(difference)
    absoluteImg = cv2.absdiff(box7x7,box3x3)
   
    #subtracting the original image from the resultant absolute image
    resultant = cv2.subtract(img,absoluteImg)
    # plt.imshow(resultant,cmap="gray")
    # plt.show()
    return resultant
    
    # plt.imshow(box7x7,cmap="gray")
    # plt.show()

c = count()
res = filtering()
x = np.arange(256)
plt.xlabel("Intensity range")
plt.ylabel("Frequency value")
plt.title("Frequency of each intensity value")
plt.plot(x,c)
plt.show()
plt.imshow(res ,cmap="gray")
plt.title("Subtracted image difference")
plt.show()
# # plt.hist(c)
#
# plt.show()