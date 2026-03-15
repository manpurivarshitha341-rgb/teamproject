from django.shortcuts import render
from .models import Voter


def dashboard(request):
    return render(request, "dashboard.html")


def register_voter(request):

    if request.method == "POST":
        name = request.POST.get("name")
        voter_id = request.POST.get("voter_id")

        face_image = request.FILES.get("face_image")
        iris_image = request.FILES.get("iris_image")

        Voter.objects.create(
            name=name,
            voter_id=voter_id,
            face_image=face_image,
            iris_image=iris_image
        )

    return render(request, "voter_register.html")


def voter_list(request):

    voters = Voter.objects.all()

    return render(request, "voter_list.html", {"voters": voters})