from django.shortcuts import redirect, reverse, render
from django.views.generic import TemplateView, CreateView, FormView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CustomUserCreationForm
from django.conf import settings
from .models import Question, Answer
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
class IndexView(TemplateView):
    template_name = 'dash/index.html'


@method_decorator(login_required, name='dispatch')
class DispatcherView(TemplateView):
    template_name = 'dash/dispatcher/dispatcher.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_question'] = Question.objects.all()[0]
        context['questions'] = Question.objects.all()[1:6]
        return context



@method_decorator(login_required, name='dispatch')
class ResearcherView(TemplateView):
    template_name = 'dash/researcher/researcher.html'

@method_decorator(login_required, name='dispatch')
class QuestionCreateView(CreateView):
    template_name = 'dash/dispatcher/question/create.html'
    model = Question
    fields = ['text', 'duration_value', 'duration_factor']
    success_url = '/dispatcher/'

    def form_valid(self, form):
        q = form.save(commit=False)
        q.dispatcher = self.request.user
        q.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class QuestionUpdateView(UpdateView):
    template_name = 'dash/dispatcher/question/create.html'
    model = Question
    fields = ['text', 'duration_value', 'duration_factor']
    success_url = '/dispatcher/'

    def form_valid(self, form):
        self.object.update(form.cl)


@method_decorator(login_required, name='dispatch')
class QuestionDeleteView(DeleteView):
    model = Question
    fields = ['text', 'duration_value', 'duration_factor']
    success_url = '/dispatcher/'

