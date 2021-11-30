from Pybuilder.src.main.python.ContrastBrightness import check
import unittest
import cv2
 
class Test(unittest.TestCase):
    def test1(self):
        image1 = cv2.imread("IMAGE/1.jpg")
        self.assertEqual(check(image1),"High brightness and Low contrast")
    def test2(self):
        image2 = cv2.imread("IMAGE/2.jpg")
        self.assertEqual(check(image2),"Low brightness and High contrast")
    def test3(self):
        image3 = cv2.imread("IMAGE/3.jpg")
        self.assertEqual(check(image3),"High brightness and High contrast")
    def test4(self):
        image4 = cv2.imread("IMAGE/4.jpg")
        self.assertEqual(check(image4),"High brightness and High contrast")
    def test5(self):
        image5 = cv2.imread("IMAGE/5.jpg")
        self.assertEqual(check(image5),"High brightness and High contrast")
    def test6(self):
        image6 = cv2.imread("IMAGE/6.jpg")
        self.assertEqual(check(image6),"Low brightness and Low contrast")
    def test7(self):
        image7 = cv2.imread("IMAGE/7.jpg")
        self.assertEqual(check(image7),"Low brightness and High contrast")
    def test8(self):
        image8 = cv2.imread("IMAGE/8.jpg")
        self.assertEqual(check(image8),"Low brightness and Low contrast")
    def test9(self):
        image9 = cv2.imread("IMAGE/9.jpg")
        self.assertEqual(check(image9),"High brightness and High contrast")
    def test10(self):
        image10 = cv2.imread("IMAGE/10.jpg")
        self.assertEqual(check(image10),"High brightness and High contrast")
if __name__ == '__main__':
    unittest.main()