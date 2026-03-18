import face_recognition

def verify_face(registered_face_path, captured_face_path):

    known_image = face_recognition.load_image_file(registered_face_path)
    unknown_image = face_recognition.load_image_file(captured_face_path)

    known_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([known_encoding], unknown_encoding)

    return results[0]