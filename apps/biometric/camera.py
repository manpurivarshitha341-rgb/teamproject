import cv2

def capture_face():

    camera = cv2.VideoCapture(0)

    while True:
        ret, frame = camera.read()

        cv2.imshow("Face Scan - Press S", frame)

        key = cv2.waitKey(1)

        if key == ord('s'):
            cv2.imwrite("captured_face.jpg", frame)
            break

    camera.release()
    cv2.destroyAllWindows()

    return "captured_face.jpg"