from .models import Vote

def count_votes():

    results = {}

    votes = Vote.objects.all()

    for vote in votes:

        if vote.candidate not in results:
            results[vote.candidate] = 0

        results[vote.candidate] += 1

    return results