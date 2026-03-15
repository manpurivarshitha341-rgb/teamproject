import cv2
import numpy as np


def preprocess_eye(image_path):
    """
    Read image and convert to grayscale for iris detection
    """

    img = cv2.imread(image_path)

    if img is None:
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # reduce noise
    gray = cv2.GaussianBlur(gray, (7, 7), 0)

    return gray


def detect_iris(image_path):
    """
    Detect iris circle using Hough Circle Transform
    """

    gray = preprocess_eye(image_path)

    if gray is None:
        return False

    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1.5,
        minDist=50,
        param1=100,
        param2=30,
        minRadius=20,
        maxRadius=80
    )

    if circles is not None:
        return True
    else:
        return False


def extract_iris_region(image_path):
    """
    Extract the iris region from the image
    """

    img = cv2.imread(image_path)

    if img is None:
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1.5,
        minDist=50,
        param1=100,
        param2=30,
        minRadius=20,
        maxRadius=80
    )

    if circles is None:
        return None

    circles = np.uint16(np.around(circles))

    for x, y, r in circles[0]:
        iris = img[y-r:y+r, x-r:x+r]
        return iris

    return None


def verify_iris(stored_image, captured_image):
    """
    Basic iris verification by detecting iris in both images
    """

    iris1 = detect_iris(stored_image)
    iris2 = detect_iris(captured_image)

    if iris1 and iris2:
        return True
    else:
        return False