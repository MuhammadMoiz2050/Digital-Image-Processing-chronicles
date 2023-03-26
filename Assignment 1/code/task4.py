from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def FlipImg(img,x):
    vertical = img.transpose(Image.FLIP_TOP_BOTTOM)
    #vertical.show()
    plt.title("Vertical")
    plt.imshow(vertical)
    plt.show()

    horizontal = img.transpose(Image.FLIP_LEFT_RIGHT)
    #horizontal.show()
    plt.title("Horizontal")
    plt.imshow(horizontal)
    plt.show()

img = Image.open(r"C:\Users\Moiz\Desktop\dip assignment 1\data\car.jpg")
plt.title("Original")
plt.imshow(img)
plt.show()
val = input("Enter either 0 or 1: ")

FlipImg(img,val)