from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.base import ContentFile

from .models import Candidate, Vote
from apps.voters.models import Voter

from apps.biometric.face_service import match_face
from apps.biometric.hybrid_matcher import verify_voter

import base64
import json


# Voting Page
def vote(request):

    candidates = Candidate.objects.all()
    message = ""

    if request.method == "POST":

        voter_id = request.POST.get("voter_id")
        candidate_id = request.POST.get("candidate")
        image_data = request.POST.get("captured_image")

        try:
            voter = Voter.objects.get(voter_id=voter_id)

            if voter.has_voted:
                message = "You already voted"
                return render(request, "voting_screen.html", {"candidates": candidates, "message": message})

            # Convert base64 image
            format, imgstr = image_data.split(';base64,')
            captured = ContentFile(base64.b64decode(imgstr), name='capture.png')

            # Face verification
            if match_face(voter.face_image.path, captured):

                candidate = Candidate.objects.get(id=candidate_id)

                Vote.objects.create(
                    voter=voter,
                    candidate=candidate
                )

                voter.has_voted = True
                voter.save()

                message = "Biometric verified. Vote submitted!"

            else:
                message = "Face not matched"

        except:
            message = "Invalid voter ID"

    return render(request, "voting_screen.html", {"candidates": candidates, "message": message})


# Results Page
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


# Face + Iris Verification API
def verify(request):

    data = json.loads(request.body)
    image = data["image"]

    # Save captured image
    format, imgstr = image.split(';base64,')
    imgdata = base64.b64decode(imgstr)

    with open("media/captured.png", "wb") as f:
        f.write(imgdata)

    result = verify_voter(
        "media/voter_images/registered.png",
        "media/captured.png"
    )

    if result:
        return JsonResponse({"message": "Verification Success"})
    else:
        return JsonResponse({"message": "Verification Failed"})