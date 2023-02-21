import easyocr
import cv2
import matplotlib.pyplot as plt

reader = easyocr.Reader(['en'], gpu=False)

image = cv2.imread('/home/hacker/Documents/ocr_learning/1.jpeg')


result = reader.readtext(image, detail=1, paragraph=False)


for (bbox, text, prob) in result:
    
    (t1, tr, br, b1,) = bbox
    t1 = (int(t1[0]),int(t1[1]))
    tr = (int(t1[0]),int(t1[1]))
    br = (int(t1[0]),int(t1[1]))
    b1 = (int(t1[0]),int(t1[1]))
    
    top_left = tuple(result[0][0][0])
    bottom_right = tuple(result[0][0][2])
    
    text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
      
    # cv2.rectangle(image, top_left, bottom_right, (0,255,0),3)
    cv2.putText(image,text, (t1[0],t1[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255),2)
    
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)    
plt.imshow(image)
plt.show()



# print(result)


