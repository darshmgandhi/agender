import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.exposure import is_low_contrast
import glob

def brightness(image, dim=10, thresh=0.5):
    L, A, B = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2LAB))
    L = L/np.max(L)
    return np.mean(L) > thresh

def contrast(image):
    return is_low_contrast(image, fraction_threshold=0.40, lower_percentile=1, upper_percentile=99, method='linear')

path = glob.glob("IMAGE/*.jpg")
def check(image):
    if (brightness(image)==True and contrast(image)==True):
        return("High brightness and High contrast")
    elif (brightness(image)==True and contrast(image)==False):
        return("High brightness and Low contrast")
    elif (brightness(image)==False and contrast(image)==True):
        return("Low brightness and High contrast")
    elif (brightness(image)==False and contrast(image)==False):
        return("Low brightness and Low contrast")
for image in path:
    image = cv2.imread(image)
    result = check(image) 
    print(result)   
    #cv2.putText(image, "{}".format(text), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    #plt.figure(figsize=(10,10))
    #plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    #plt.show()

