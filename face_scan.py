import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    cv2.imshow("Face Scan - Press S to Capture", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):  # press S to capture
        cv2.imwrite("captured_face.jpg", frame)
        break

camera.release()
cv2.destroyAllWindows()