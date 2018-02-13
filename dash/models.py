from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    text = models.TextField()
    time_posted = models.DateTimeField(auto_now_add=True)
    duration_value = models.IntegerField()
    UNITS = (
        (60, 'min'),
        (1, 'sec')
    )
    duration_factor = models.IntegerField(choices=UNITS, default=60)
    dispatcher = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    @property
    def time_done(self):
        seconds = self.duration_value * self.duration_factor
        return self.time_posted + timezone.timedelta(seconds=seconds)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    researcher = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    text = models.TextField()
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    # TODO think about cool statistics to store in here

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()