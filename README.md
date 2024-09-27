# **Text Recognition in License Plate Using OpenCV (Python)**

## GOAL:
**To extract the license plate number from the image by performing various image processing techniques.**
 
## FLOW:

  ### Step #1: Read Image
  
  > Read image from the directory.
    
  ### Step #2: Convert to grayscale image
  
  > convert the image to grayscale. in order to extract good details from the image.
    
  ### Step #3: Masking

  > To exclude unwanted parts from the image.

  ### Step #4: Gaussian Blur

  > Gaussian Blur is performed to Smoothen the Image

  ### Step #5: Adaptive Thresholding

  > Set a threshold value and perform thresholding. so that we can seperate the main object 
from the background.

  ### Step #6: Erosion

  > Perform erosion to reduce the noise in the image

  ### Step #7: Dilation

  > Perform dilation to increase the edge thickness. so that it will be easier for the OCR to 
  extract text.

  ### Step #8: OCR (Using Tesseract OCR)
  
  > Apply OCR( optical character recognition) to extract text from the processed image.

  ### Step #9: Print Extracted License Number
  > Prints the Extracted text extracted from the dilated number plate image.

  







  
    


    

