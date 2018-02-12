from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    text = models.TextField()
    time_posted = models.TimeField(auto_now_add=True)
    dispatcher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    researcher = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_posted = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # TODO think about cool statistics to store in here