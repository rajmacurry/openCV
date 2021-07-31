import cv2

#reading an image
img = cv2.imread('lena.jpg', -1) #reading an image, first argument is image name, second is flag
#if flag == 1, load color image
#if flag == 0, load grayscale image
#if flag == -1, load image with alpha channels

print(img)  #prints matrix

cv2.imshow('image', img) #first is the window, second is the image variable
cv2.waitKey(0)   #argument is delay time in millisecond. if you put 0, infinite delay
cv2.destroyAllWindows()

#writing an image
#cv2.imwrite('lena_copy.png',img)

#if Esc is pressed, we close window, if S is pressed, we save the image
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s' or 'S'):
    cv2.imwrite('lena_copy.png',img)
    cv2.destroyAllWindows()

