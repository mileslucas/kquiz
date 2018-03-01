from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import Question, Answer


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label="First Name", required=True,
        help_text="Required.")
    last_name = forms.CharField(max_length=100, label="Last Name", required=True,
                                 help_text="Required.")

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['text', 'duration_value', 'duration_factor']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']
