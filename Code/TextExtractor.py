import cv2 as cv
import numpy as np
import pytesseract as pyt
#read image.
image=cv.imread(r'C:\Users\raghu\OneDrive\Documents\OpenCV\projects\Text extraction in License Plate\assets\Images\new number plate clean.jpg')

#raise a value error if you can't read the image.
if image is None:
    raise ValueError("\033[31m [ATTENTION] COUDN'T ABLE TO FIND THE IMAGE\033[0m")
    exit()
else:
    print("\033[92m SUCCESS IMAGE IS SUCCESSFULLY READ \033[0m")

#Convert the image to Gray Scale Image
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
# Apply a mask to remove the top and bottom text (like 'California' and 'dmv.ca.gov')
# Masking the top
height, width = gray.shape
mask = np.ones((height, width), dtype=np.uint8) * 255  # Create a white mask
cv.rectangle(mask, (0, 0), (width, int(height*0.1)), 0, -1)  # Black out top part
cv.rectangle(mask, (0, int(height*0.855)), (width, height), 0, -1)  # Black out bottom part
cv.rectangle(mask, (0, 0), (int(width * 0.12), height), 0, -1)  # Black out left side
cv.rectangle(mask,(int(width*0.95),0),(width,height),0,-1) # Black out Right side

# Apply mask to image
masked_img = cv.bitwise_and(gray, mask)

# Apply Gaussian Blur to reduce noise
gray_Gblur = cv.GaussianBlur(masked_img, (5, 5), 0)

#Applying adaptive thresholding for better results in variable lighting.
#syntax = cv2.adaptiveThreshold(source image, maxValue, adaptiveMethod, thresholdType, blockSize, C)
threshold=cv.adaptiveThreshold(gray_Gblur,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,15,3)

#Applying Erosion to reduce noise.
kernel = np.ones((2, 2), np.uint8) #setting up the structured element matrix. which slides over each pixel of the image and erode it.
eroded_img = cv.erode(threshold, kernel, iterations=1)
#kernel = np.ones((8, 8), np.uint8)
#Applying dilation to thicken the edges
dilated_img = cv.dilate(eroded_img, kernel, iterations=3)
#OCR for extracting text from dilated image
text = pyt.image_to_string(dilated_img, config='--psm 7 --oem 3') #psm 7 for single line of text 
print("\033[92m License Plate Number: \033[93m", text,"\033[0m")



cv.imshow('License Plate',eroded_img)
#cv.imshow('License Plate',dilated_img)
cv.waitKey(0)
cv.destroyAllWindows()
