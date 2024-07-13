import cv2
import matplotlib.pyplot as plt

# Read single frame avi
cap = cv2.VideoCapture('natgeo.jpeg')
rval, frame = cap.read()

# Attempt to display using cv2 (doesn't work)
cv2.namedWindow("Input")
cv2.imshow("Input", frame)

#Display image using matplotlib (Works)
b,g,r = cv2.split(frame)
frame_rgb = cv2.merge((r,g,b))
plt.imshow(frame_rgb)
plt.title('Matplotlib') #Give this plot a title, 
                        #so I know it's from matplotlib and not cv2
plt.show()