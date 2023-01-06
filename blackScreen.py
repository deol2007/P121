import numpy as np
import cv2

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

video_cap = cv2.VideoCature(0)

for i in range(60):
    ret,bg = video_cap.read()
bg = np.flip(bg, axis=1)

while (video_cap.isOpened()):
    ret, img = video_cap.read()
    if not ret:
        break
    img = np.flip(img,axis=1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

l_black = np.array([30, 30, 0])
u_black = np.array([104, 153, 70])

lower_black = np.array([30, 30, 0])
upper_black = np.array([104, 153, 70])
mask = cv2.inRange(hsv, lower_black, upper_black)

mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

video_cap.release()
cv2.destroyAllWindows()