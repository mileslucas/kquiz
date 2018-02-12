from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    model = User
    fields = ['username', 'password', 'first_name', 'last_name']
    success_url = 'login'

@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'dash/index.html'


@method_decorator(login_required, name='dispatch')
class DispatcherView(TemplateView):
    template_name = 'dash/dispatcher/dispatcher.html'


@method_decorator(login_required, name='dispatch')
class ResearcherView(TemplateView):
    template_name = 'dash/researcher/researcher.html'

