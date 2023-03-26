from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


img1 = Image.open(r"C:\Users\Moiz\Desktop\dip assignment 1\data\rect1.jpg")
img2 = Image.open(r"C:\Users\Moiz\Desktop\dip assignment 1\data\rect1.jpg")

def StackHorizontal(img1,img2):
        if img1.size == img2.size:
           newImg = Image.new("RGB", (758, 277), "white")
           newImg.paste(img1,(0,0))
           newImg.paste(img2,(379,0))
           #plt.imshow(newImg)
           #plt.show()
           print("Modified Img size: ",newImg.size)
           newImg.show()


print("Image Sizes: ",img1.size,img2.size) 
print("Image Formats: ",img1.format,img2.format)  
StackHorizontal(img1,img2)