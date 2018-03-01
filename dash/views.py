from django.shortcuts import redirect, reverse, render, Http404
from django.views.generic import TemplateView, CreateView, FormView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.decorators import method_decorator
from .forms import CustomUserCreationForm, QuestionForm
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
        context['questions'] = [q for q in Question.objects.order_by('-time_posted') if q.completed][:3]
        context['add_question_form'] = QuestionForm
        return context


@method_decorator(login_required, name='dispatch')
class QuestionListView(ListView):
    template_name = 'dash/question/list.html'
    model = Question
    ordering = '-time_posted'


@method_decorator(login_required, name='dispatch')
class QuestionCreateView(CreateView):
    template_name = 'dash/question/create.html'
    model = Question
    fields = ['text', 'duration_value', 'duration_factor']
    success_url = '/'

    def form_valid(self, form):
        q = form.save(commit=False)
        q.creator = self.request.user
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
        if not obj.creator == self.request.user:
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
        if not obj.creator == self.request.user:
            raise Http404
        return obj


@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    template_name = 'dash/profile/detail.html'
    model = User
    slug_field = 'username'

@method_decorator(login_required, name='dispatch')
class AnswerCreateView(CreateView):
    template_name = 'dash/answer/create.html'
    model = Answer
    fields = ['text']
    success_url = '/'

    def form_valid(self, form):
        a = form.save(commit=False)
        a.responder = self.request.user
        q_id = self.request.path.split('/')[-1]
        a.question = Question.objects.get(id=q_id)
        a.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class AnswerUpdateView(UpdateView):
    template_name = 'dash/answer/update.html'
    model = Answer
    fields = ['text']
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super().get_object()
        if not obj.responder == self.request.user:
            raise Http404
        return obj


@method_decorator(login_required, name='dispatch')
class AnswerDeleteView(DeleteView):
    template_name = 'dash/answer/delete.html'
    model = Answer
    success_url = '/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super().get_object()
        if not obj.responder == self.request.user:
            raise Http404
        return obj