from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2

# img1 = Image.open(r"C:\Users\Moiz\Desktop\dip assignment 1\data\rect1.jpg")
# img2 = Image.open(r"C:\Users\Moiz\Desktop\dip assignment 1\data\rect7.jpg")

img1 = cv2.imread(r"C:\Users\Moiz\Desktop\dip assignment 1\data\rect1.jpg",cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(r"C:\Users\Moiz\Desktop\dip assignment 1\data\rect7.jpg",cv2.IMREAD_GRAYSCALE)

def CommonImg(img1, img2):
    print(img1.shape)
    newImg = np.zeros(shape = (277,379))
    print(newImg.shape)
    for i in range(0,img1.shape[0]):
        for j in range(0,img1.shape[1]):
            if img1[i][j] == img2[i][j]:
                newImg[i][j] = img1[i][j] 

    cv2.imshow("Window",newImg)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

CommonImg(img1,img2)