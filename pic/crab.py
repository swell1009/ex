#!/usr/local/bin/python

from PIL import ImageGrab

#get current screen copy
image = ImageGrab.grab()

#display image size
print("Current screen shot size :",image.size)

#display image mode
print("Screen shot picture mode :", image.mode)

#save picture to /tmp/screen-grab-1.bmp
#image.save('/tmp/screen-grab-1.bmp')

#show picture
image.show()
