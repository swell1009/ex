from PIL import Image
import math
import operator
from functools import reduce


def image_contrast(img1, img2):

    image1 = Image.open(img1)
    image2 = Image.open(img2)

    h1 = image1.histogram()
    print(h1)
    h2 = image2.histogram()
    print(h2)

    result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return result

if __name__ == '__main__':
    img1 = "1.jpg"  # 指定图片路径
    img2 = "1.jpg"
    result = image_contrast(img1,img2)
    print(result)