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
]