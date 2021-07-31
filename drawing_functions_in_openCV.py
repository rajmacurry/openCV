import numpy as np
import cv2

# img = cv2.imread('lena.jpg',1)
# we can create image to an numpy array as well. using np.zeros
img = np.zeros([512, 512, 3], np.uint8)
# ([height, width, no_of_color_channels], datatype)

#img = np.ones([512, 512, 3], np.uint8)*255
#this gives white background

pts = np.array([[255,10],[300,60],
               [300,110],[255,160],
               [210,110],[210,60]])
img = cv2.polylines(img, [pts], True, (255,0,0))

img = cv2.line(img, (0,0), (255,255), (4,219,204), 3)
img = cv2.arrowedLine(img, (511,0), (255,255), (204,219,4), 3)

img = cv2.rectangle(img, (255,255), (511,511), (4,0,204), 1)
img = cv2.rectangle(img, (0,255), (255,511), (4,0,199), -11)

img = cv2.circle(img, (255,255), 100, (255,255,255), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'openCV', (10,150), font, 1, (0,0,0), 1, cv2.LINE_4)



cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
