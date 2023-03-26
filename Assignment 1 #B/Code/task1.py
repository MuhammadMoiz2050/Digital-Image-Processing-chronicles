import cv2
import numpy 

#Image.open()
img = cv2.imread(r"G:\University Stuff\8th semester\Dip\Assignment#1-(B)\data\dental_xray.tif",cv2.IMREAD_GRAYSCALE)
ret, thresh=cv2.threshold(img, 140, 255, cv2.THRESH_BINARY)

#Applying a mask for highlighting the white parts of the teeth
threshold_value = 245
ret, thresh1=cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

white_highlight = cv2.bitwise_and(img, img, mask=thresh1)

#Changing the colour of the highlighted areas to red 
white_highlight_red = cv2.cvtColor(white_highlight, cv2.COLOR_GRAY2BGR)
white_highlight_red[:, :, 0] = 0
white_highlight_red[:, :, 1] = 0

# Invert the mask to highlight the non-white regions in black
mask_inv = cv2.bitwise_not(thresh1)

# Convert the grayscale image to a 3-channel image
img_masked = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# Apply the inverted mask to the original image
img_masked = cv2.bitwise_and(img_masked, img_masked, mask=mask_inv)

# Blend the masked original image with the white highlighted image
blended_image = cv2.addWeighted(img_masked, 1, white_highlight_red, 0.5, 0)
#added = cv2.add(white_highlight_red,img1)

#finding the percentage of affected pixels for the highlighting technique
def percentageCalculate():
    total_pixels = img.shape[0]*img.shape[1]
    #print(img.shape[0],img.shape[1])
    affected_pixels = cv2.countNonZero(thresh1)
    percentage = (affected_pixels/total_pixels)*100
    print("Percentage of the pixels affected in this image: ",percentage,"%")

percentageCalculate()
cv2.imshow("Separated teeth",thresh)
cv2.imshow("Highlited image", blended_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
