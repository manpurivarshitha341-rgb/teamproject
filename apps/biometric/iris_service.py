import cv2
import os

def match_iris(captured_file):

    voters_dir = "media/voters/"
    captured_img = cv2.imread(captured_file, cv2.IMREAD_GRAYSCALE)

    if captured_img is None:
        return False, "No iris image captured"

    for file in os.listdir(voters_dir):

        if "iris" not in file.lower():
            continue

        path = os.path.join(voters_dir, file)
        voter_img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

        if voter_img is None:
            continue

        voter_img = cv2.resize(voter_img, (captured_img.shape[1], captured_img.shape[0]))

        result = cv2.matchTemplate(captured_img, voter_img, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)

        if max_val > 0.7:
            return True, file

    return False, "No iris match"