import cv2
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 1080)    #set width
cap.set(4, 720)     #set height

#the set width and set height depends on your camera.
#if applied random resolution, it will set to closest resolution available.

print(cap.get(3))
print(cap.get(4))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
