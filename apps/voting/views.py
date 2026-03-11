from django.shortcuts import render
from .models import Candidate, Vote
from apps.voters.models import Voter

from apps.biometric.camera import capture_face_image
from apps.biometric.face_service import match_face

from apps.biometric.iris_camera import capture_iris_image
from apps.biometric.iris_service import match_iris


def vote(request):

    candidates = Candidate.objects.all()
    message = ""

    if request.method == "POST":

        voter_id = request.POST.get("voter_id")
        candidate_id = request.POST.get("candidate")

        try:
            voter = Voter.objects.get(id=voter_id)

            # Check duplicate vote
            if Vote.objects.filter(voter=voter).exists():
                message = "You already voted!"
                return render(request,"vote.html",{"candidates":candidates,"message":message})

            # FACE CHECK
            face_file = capture_face_image()
            face_match, face_result = match_face(face_file)

            if not face_match:
                message = "Face verification failed!"
                return render(request,"vote.html",{"candidates":candidates,"message":message})

            # IRIS CHECK
            iris_file = capture_iris_image()
            iris_match, iris_result = match_iris(iris_file)

            if not iris_match:
                message = "Iris verification failed!"
                return render(request,"vote.html",{"candidates":candidates,"message":message})

            # Save vote
            candidate = Candidate.objects.get(id=candidate_id)
            Vote.objects.create(voter=voter, candidate=candidate)

            message = "Vote submitted successfully!"

        except:
            message = "Invalid voter ID"

    return render(request,"vote.html",{
        "candidates": candidates,
        "message": message
    })
def results(request):

    candidates = Candidate.objects.all()

    data = []

    for c in candidates:
        count = Vote.objects.filter(candidate=c).count()
        data.append({
            "name": c.name,
            "party": c.party,
            "votes": count
        })

    return render(request, "results.html", {"data": data})