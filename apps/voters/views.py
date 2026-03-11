from django.shortcuts import render
from .models import Voter


def register_voter(request):
    if request.method == "POST":
        name = request.POST.get("name")
        voter_id = request.POST.get("voter_id")
        face = request.FILES.get("face")
        iris = request.FILES.get("iris")

        Voter.objects.create(
            name=name,
            voter_id=voter_id,
            face=face,
            iris=iris
        )

    return render(request, "voter_register.html")


def voter_list(request):
    voters = Voter.objects.all()
    return render(request, "voter_list.html", {"voters": voters})