import os

import cv2

#read image
image_path= os.path.join('.','data','noob.png')

img= cv2.imread(image_path)

#write image
cv2.imwrite(os.path.join('.','data','noob_out.png'),img)

#visualize image
cv2.imshow('image',img)
cv2.waitKey(5000) #waitKey is to the amount of time to wait for the dialouge box to be there, i.e. 5000 means 5000msi.e.5seconds
# cv2.waitKey(0) it would be open till you press zero.


