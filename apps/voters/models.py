from django.db import models

class Voter(models.Model):
    voter_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    has_voted = models.BooleanField(default=False)