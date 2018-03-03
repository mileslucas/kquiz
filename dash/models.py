from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    number = models.IntegerField(verbose_name='Question Number')
    text = models.TextField(verbose_name='Question')
    time_posted = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(verbose_name='Points')
    our_answer = models.CharField(max_length=100, default='')
    correct = models.BooleanField(default=False)
    duration_value = models.IntegerField(default=6, verbose_name='Duration')
    UNITS = (
        (60, 'min'),
        (1, 'sec')
    )
    correct_answer = models.CharField(max_length=100, default='')
    duration_factor = models.IntegerField(choices=UNITS, default=60)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    @property
    def time_done(self):
        seconds = self.duration_value * self.duration_factor
        return self.time_posted + timezone.timedelta(seconds=seconds)
    @property
    def completed(self):
        return self.time_done < timezone.now()
    @property
    def time_left(self):
        return self.time_done - timezone.now()
    @property
    def percent_left(self):
        p = (self.time_done - timezone.now()).total_seconds() / (self.time_done - self.time_posted).total_seconds()
        return int(p * 100)

    @property
    def effective_points(self):
        return self.points if self.correct else 0

    def __str__(self):
        return f'Question {self.number}'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, editable=False)
    responder = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    text = models.CharField(max_length=800, verbose_name='Answer')
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Event')
    location = models.CharField(max_length=200, verbose_name='Location')
    time = models.CharField(max_length=100, verbose_name='When')
    description = models.TextField(default='', verbose_name='Description (Optional)')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    respondents = models.ManyToManyField(User, related_name="events", default=None)
    completed = models.BooleanField(default=False)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    # TODO think about cool statistics to store in here
    def __str__(self):
        return self.user.get_full_name()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
