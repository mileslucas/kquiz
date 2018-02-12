from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dispatcher/', DispatcherView.as_view(), name='dispatcher'),
    path('researcher/', ResearcherView.as_view(), name='researcher')
]