from django.db import models


# Create your models here.
class Job(models.Model):
    # Intellij wanted this below
    def __init__(self):
        pass

    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
