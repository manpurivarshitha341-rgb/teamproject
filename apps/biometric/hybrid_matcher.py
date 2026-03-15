from .face_service import match_face
from .iris_service import detect_iris

def verify_voter(face_db, captured):

    face_match = match_face(face_db, captured)

    iris_match = detect_iris(captured)

    if face_match and iris_match:
        return True
    else:
        return False