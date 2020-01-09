
import pytesseract
from pytesseract import Output
import cv2
import os

filepath = r'C:\python_projects\pdf_data_extraction\pdf_data_extraction\pdf_images'
filename = '00a7d8b0-5279-4b1d-82e8-122ad6d832e0-02.jpg'
img = cv2.imread(os.path.join(filepath, filename))

d = pytesseract.image_to_data(img, output_type=Output.DICT)
n_boxes = len(d['level'])
print(d.keys())
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    if d['text'][i] != '':
        print(d['text'][i], d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
