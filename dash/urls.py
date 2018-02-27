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
    path('question/<int:pk>/update', QuestionUpdateView.as_view(), name='update_question'),
    path('question/<int:pk>/remove', QuestionDeleteView.as_view(), name='remove_question'),
    # path('<int:pk>', ResearcherView.as_view(), name='add_answer'),
]