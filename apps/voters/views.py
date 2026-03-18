from django.shortcuts import render
from .models import Voter


def dashboard(request):
    return render(request, "dashboard.html")


def register_voter(request):

    if request.method == "POST":
        name = request.POST.get("name")
        voter_id = request.POST.get("voter_id")
        age = request.POST.get("age")
        gender= request.POST.get("gender")

        Voter.objects.create(
    voter_id=voter_id,
    name=name,
      age=age,
     gender=gender
)

    

        


        

    return render(request, "voter_register.html")


def voter_list(request):

    voters = Voter.objects.all()

    return render(request, "voter_list.html", {"voters": voters})