from django.shortcuts import redirect, reverse, render, Http404
from django.views.generic import TemplateView, CreateView, FormView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from .forms import CustomUserCreationForm
from django.conf import settings
from .models import Question, Answer, Profile
from django.utils import timezone

class RegisterView(FormView):
    redirect_authenticated_user = True
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = '/login/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class DashView(TemplateView):
    template_name = 'dash/dash.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cqs'] = [q for q in Question.objects.all() if not q.completed]
        context['questions'] = [q for q in Question.objects.order_by('-time_posted') if q.completed][:5]
        return context

@method_decorator(login_required, name='dispatch')
class QuestionListView(ListView):
    template_name = 'dash/question/list.html'
    model = Question

@method_decorator(login_required, name='dispatch')
class QuestionCreateView(CreateView):
    template_name = 'dash/question/create.html'
    model = Question
    fields = ['text', 'duration_value', 'duration_factor']
    success_url = '/'

    def form_valid(self, form):
        q = form.save(commit=False)
        q.dispatcher = self.request.user
        q.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class QuestionDetailView(DetailView):
    template_name = 'dash/question/detail.html'
    model = Question
    fields = ['text', 'duration_value', 'duration_factor']

@method_decorator(login_required, name='dispatch')
class QuestionUpdateView(UpdateView):
    template_name = 'dash/question/update.html'
    model = Question
    fields = ['text', 'duration_value', 'duration_factor']
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super().get_object()
        if not obj.dispatcher == self.request.user:
            raise Http404
        return obj


@method_decorator(login_required, name='dispatch')
class QuestionDeleteView(DeleteView):
    template_name = 'dash/question/delete.html'
    model = Question
    success_url = '/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super().get_object()
        if not obj.dispatcher == self.request.user:
            raise Http404
        return obj


@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    template_name = 'dash/profile/detail.html'
    model = User
    slug_field = 'username'
