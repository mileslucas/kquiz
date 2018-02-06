from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    def get(self, request, **kwargs):
        return HttpResponse('result')


@method_decorator(login_required, name='dispatch')
class LeaderView(TemplateView):
    template_name = 'index.html'

    def get(self, request, **kwargs):
        return HttpResponse('result')


@method_decorator(login_required, name='dispatch')
class WorkerView(TemplateView):
    template_name = 'index.html'

    def get(self, request, **kwargs):
        return HttpResponse('result')
