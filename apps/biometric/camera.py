import cv2

def capture_face_image(filename="face_capture.jpg"):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Capture Face")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow("Capture Face", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:  # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:  # SPACE pressed
            cv2.imwrite(filename, frame)
            print(f"{filename} saved!")
            break

    cam.release()
    cv2.destroyAllWindows()
    return filename