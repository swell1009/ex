import cv2 as cv

face_patterns = cv.CascadeClassifier(
    '/usr//Users/xiangzhang/anaconda3/pkgs/libopencv-3.4.1-h0f2e407_1/opencv3/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

sample_image = cv.imread('/Users/xiangzhang/Desktop/TestPic.jpg')

faces = face_patterns.detectMultiScale(sample_image,
                                       scaleFactor=1.1,
                                       minNeighbors=5,
                                       minSize=(100, 100))

for (x, y, w, h) in faces:
    cv.rectangle(sample_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
