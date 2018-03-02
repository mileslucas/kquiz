from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .views import *


urlpatterns = [
    path('', DashView.as_view(), name='dash'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/<slug>', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('question', QuestionListView.as_view(), name='questions'),
    path('question/add', QuestionCreateView.as_view(), name='add_question'),
    path('question/<int:pk>', QuestionDetailView.as_view(), name='detail_question'),
    path('question/update/<int:pk>', QuestionUpdateView.as_view(), name='update_question'),
    path('question/remove/<int:pk>', QuestionDeleteView.as_view(), name='remove_question'),
    path('answer/add/<int:pk>', AnswerCreateView.as_view(), name='add_answer'),
    path('answer/update/<int:pk>', AnswerUpdateView.as_view(), name='update_answer'),
    path('answer/remove/<int:pk>', AnswerDeleteView.as_view(), name='remove_answer'),
    path('events', EventListView.as_view(), name='events'),
    path('event/add', EventCreateView.as_view(), name='add_event'),
    path('event/update/<int:pk>', EventUpdateView.as_view(), name='update_event'),
    path('event/remove/<int:pk>', EventDeleteView.as_view(), name='remove_event'),
]