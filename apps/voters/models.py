from django.db import models

class Voter(models.Model):
    name = models.CharField(max_length=100)
    voter_id = models.CharField(max_length=50, unique=True)

    face_image = models.ImageField(upload_to='voters/')
    iris_image = models.ImageField(upload_to='voters/')

    has_voted = models.BooleanField(default=False)

    def __str__(self):
        return self.name