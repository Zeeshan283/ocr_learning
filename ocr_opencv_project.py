import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np


reader =  easyocr.Reader(['en'], gpu=False)

result = reader.readtext("/home/hacker/Documents/ocr_learning/chinese_tra.jpg")



img = cv2.imread("/home/hacker/Documents/ocr_learning/chinese_tra.jpg")
for detection in result:
    top_left = tuple([int(val) for val in detection[0][0]])
    bottom_right = tuple([int(val) for val in detection[0][2]])
    text = detection[1]
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.rectangle(img ,  top_left, bottom_right, (0,255,0),5)

plt.figure(figsize=(10,10))
plt.imshow(img)
plt.show