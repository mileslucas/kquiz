from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dispatcher/', DispatcherView.as_view(), name='dispatcher'),
    path('dispatcher/question/add', QuestionCreateView.as_view(), name='add_question'),
    path('dispatcher/question/<int:pk>', QuestionDetailView.as_view(), name='detail_question'),
    path('dispatcher/question/<int:pk>/update', QuestionUpdateView.as_view(), name='update_question'),
    path('dispatcher/question/<int:pk>/remove', QuestionDeleteView.as_view(), name='remove_question'),
    path('researcher/', ResearcherView.as_view(), name='researcher'),
    path('researcher/<int:pk>', ResearcherView.as_view(), name='add_answer'),
]