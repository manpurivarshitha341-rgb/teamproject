from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Candidate


# Landing page
def vote(request):
    candidates = Candidate.objects.all()

    return render(request, "voting/vote.html", {
        "candidates": candidates
    })


# Optional start page (same as landing)
def start_vote(request):
    return render(request, "voting/start.html")


# Scan voter face/iris
def scan_face(request):
    if request.method == "POST":
        # TEMP: Set True for testing
        voter_valid = True  

        if voter_valid:
            candidates = Candidate.objects.all()

            return render(request, "voting/submit_vote.html", {
                "candidates": candidates
            })
        else:
            return render(request, "voting/scan_face.html", {
                "error": "Invalid voter"
            })

    return render(request, "voting/scan_face.html")


# Submit the vote
def submit_vote(request):
    if request.method == "POST":
        selected_candidate = request.POST.get("candidate")

        if selected_candidate:
            # 👉 You can store vote here later

            return redirect('results')
        else:
            candidates = Candidate.objects.all()

            return render(request, "voting/submit_vote.html", {
                "candidates": candidates,
                "error": "Please select a candidate"
            })

    # If user comes directly without POST
    candidates = Candidate.objects.all()

    return render(request, "voting/submit_vote.html", {
        "candidates": candidates
    })


# Show voting results
def results(request):
    candidates = Candidate.objects.all()

    results_data = []
    for candidate in candidates:
        results_data.append({
            "name": candidate.name,
            "party": candidate.party,
            "votes": 0  # You can update later with real count
        })

    return render(request, "voting/results.html", {
        "results": results_data
    })