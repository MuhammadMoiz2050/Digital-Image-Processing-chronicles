# import cv2

# def ConvertToGray(img):
#     B,G,R = img[:,:,0],img[:,:,1],img[:,:,2]
#     #print(B,G,R)
#     imgGray = 0.299*R + 0.587*G + 0.114*B
#     cv2.imshow("Gray Img",imgGray)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# img = cv2.imread(r"C:\Users\Moiz\Desktop\dip assignment 1\data\test.png",1)
# ConvertToGray(img)
# cv2.imshow("Original Img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import cv2

def ConvertToGray(img):
    R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]
    imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
    plt.imshow(imgGray, cmap='gray')
    plt.show()

img = mpimg.imread(r"C:\Users\Moiz\Desktop\dip assignment 1\data\test.png")
plt.imshow(img)
plt.show()
ConvertToGray(img)
