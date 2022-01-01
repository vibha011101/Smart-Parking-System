import cv2
import csv
import numpy as np

# select the video source; 0 - integrated webcam; 1 - external webcam;
#VIDEO_SOURCE = 0

# start the recording
#cap = cv2.VideoCapture(VIDEO_SOURCE)
#suc, image = cap.read()

# save first frame as JPEG file
#cv2.imwrite("frame0.jpg", image)
img = cv2.imread(r"C:\Users\vibha\Desktop\AI\parkimage1.jpg")
#cv2.imshow("Original",img)
#cv2.waitKey(0)

# get the regions of interest/parking spots
r =cv2.selectROIs('ROI Selector',img, showCrosshair=False, fromCenter=False)

# convert the result to a list
rlist = list(r)
print(rlist)

# write the list into a csv file
with open('data.csv', 'w', newline='') as outf:
  csvw = csv.writer(outf)
  csvw.writerows(rlist)

# when everything is done, release the capture
#cap.release()
cv2.destroyAllWindows()