import face_recognition
import os

def match_face(captured_file):
    voters_dir = "media/voters/"
    captured_image = face_recognition.load_image_file(captured_file)
    captured_encoding = face_recognition.face_encodings(captured_image)

    if not captured_encoding:
        return False, "No face detected!"

    captured_encoding = captured_encoding[0]

    # Check all voter images
    for voter_file in os.listdir(voters_dir):
        voter_image = face_recognition.load_image_file(os.path.join(voters_dir, voter_file))
        voter_encoding = face_recognition.face_encodings(voter_image)
        if not voter_encoding:
            continue
        voter_encoding = voter_encoding[0]

        matches = face_recognition.compare_faces([voter_encoding], captured_encoding)
        if matches[0]:
            return True, voter_file  # Match found

    return False, "No match found"