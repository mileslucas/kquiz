from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.TextField()
    time_posted = models.TimeField(auto_now_add=True)
    duration = models.TimeField()



    def __str__(self):
        pass