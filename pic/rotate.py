from PIL import Image
import numpy as np

src_image = Image.open('2.jpg')


dst_image = src_image.rotate(270)
#dst_image.show()
arr = np.array(dst_image)
print(arr.shape)
print(arr.dtype)
#print(arr)

gray = dst_image.convert('L')
gray.show()
arr = np.array(gray)
print(arr.shape)
print(arr.dtype)