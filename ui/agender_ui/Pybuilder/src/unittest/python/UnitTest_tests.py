from matplotlib import pyplot
from ContrastBrightness import check
import unittest
import cv2

import sys
sys.path.insert(0, '../login_signup')
from detectors import age_model, gender_model, face_detect, crop
from mtcnn.mtcnn import MTCNN
import tensorflow as tf
import numpy as np

class Test(unittest.TestCase):
    def test1(self):
        image1 = cv2.imread("../IMAGE/1.jpg")
        self.assertEqual(check(image1),"High brightness and Low contrast")
    def test2(self):
        image2 = cv2.imread("../IMAGE/2.jpg")
        self.assertEqual(check(image2),"Low brightness and High contrast")
    def test3(self):
        image3 = cv2.imread("../IMAGE/3.jpg")
        self.assertEqual(check(image3),"Low brightness and High contrast")
    def test4(self):
        image4 = cv2.imread("../IMAGE/4.jpg")
        self.assertEqual(check(image4),"High brightness and High contrast")
    def test5(self):
        image5 = cv2.imread("../IMAGE/5.jpg")
        self.assertEqual(check(image5),"High brightness and Low contrast")
    def test6(self):
        image6 = cv2.imread("../IMAGE/6.jpg")
        self.assertEqual(check(image6),"Low brightness and Low contrast")
    def test7(self):
        image7 = cv2.imread("../IMAGE/7.jpg")
        self.assertEqual(check(image7),"Low brightness and High contrast")
    def test8(self):
        image8 = cv2.imread("../IMAGE/8.jpg")
        self.assertEqual(check(image8),"Low brightness and Low contrast")
    def test9(self):
        image9 = cv2.imread("../IMAGE/9.jpg")
        self.assertEqual(check(image9),"High brightness and High contrast")
    def test10(self):
        image10 = cv2.imread("../IMAGE/10.jpg")
        self.assertEqual(check(image10),"High brightness and High contrast")

class MLTest(unittest.TestCase):

    def setUp(self):
        self.model, self.prediction_age = age_model()
        self.model_gender = gender_model()
        self.images = ['../IMAGE/image11.jpeg', '../IMAGE/image12.jpeg', '../IMAGE/image13.jpeg']
        self.age = ['0 - 5', '51 - 60', '31 - 40']
        self.gender = ['Male', 'Female', 'Female']
        self.detector = MTCNN()

    def test_age(self):
        for i in range(len(self.images)):
            with self.subTest(i = i):
                b = []
                img = pyplot.imread(self.images[i])
                faces = self.detector.detect_faces(img)
                face_detect(self.images[i], faces, b)
                crop(b, self.images[i])
                test_image = tf.expand_dims(tf.io.decode_image(tf.io.read_file("IM/resized_image.jpg"), dtype=tf.float32), axis=0)
                prediction = self.prediction_age[np.argmax(self.model.predict(test_image)[0])]
                self.assertEqual(prediction, self.age[i])

    def test_gender(self):
        for i in range(len(self.images)):
            with self.subTest(i = i):
                b = []
                img = pyplot.imread(self.images[i])
                faces = self.detector.detect_faces(img)
                face_detect(self.images[i], faces, b)
                crop(b, self.images[i])
                test_image = tf.expand_dims(tf.io.decode_image(tf.io.read_file("IM/resized_image.jpg"), dtype=tf.float32), axis=0)
                prediction = np.argmax(self.model.predict(test_image)[0])
                if prediction == 0:
                    prediction = 'Male'
                else:
                    prediction = 'Female'
                self.assertEqual(prediction, self.gender[i])

# if __name__ == '__main__':
#     unittest.main()