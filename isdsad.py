import cv2
import matplotlib.pyplot as plt

image = cv2.imread('/home/hacker/Documents/ocr_learning/chinese_tra.jpg')

# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image)
plt.show()