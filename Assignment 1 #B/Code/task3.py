import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread(r"G:\University Stuff\8th semester\Dip\Assignment#1-(B)\data\grain3.tif",cv2.IMREAD_GRAYSCALE)

def transform(img):

    # Define the logarithmic transformation function
    #c = 255 / np.log(1 + np.max(img))
    c=40
    rows = img.shape[0]
    cols = img.shape[1]
    logTransform = np.zeros(shape=(rows,cols))
    for i in range(0,rows):
        for j in range(0,cols):

            logTransform[i][j] = c * np.log(img[i][j]+1)

            # Normalize the values to 0-255 range
            logTransform = np.uint(logTransform)
    
    return logTransform
# cv2.imshow("Highlited image", logTransform)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


logTransform = transform(img)
plt.imshow(logTransform, cmap="gray", vmin=0, vmax=255)
plt.show()

# fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10,5))
# ax1.set_title('Original image')
# ax1.imshow(img, cmap='gray')
# ax2.set_title('Logarithmic transformation')
# ax2.imshow(logTransform, cmap='gray')
# plt.show()