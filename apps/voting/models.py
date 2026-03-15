from django.db import models
from apps.voters.models import Voter

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Vote(models.Model):
    voter = models.OneToOneField(Voter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    models.CharField(max_length=50)

    def __str__(self):
        return f"{self.voter.name} voted {self.candidate.name}"