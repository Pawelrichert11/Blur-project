import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('natgeo.jpeg')
rval, frame = cap.read()


b,g,r = cv2.split(frame)
frame_rgb = cv2.merge((r,g,b))
plt.imshow(frame_rgb)
plt.title('Image')
plt.show()