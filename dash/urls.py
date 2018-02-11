from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import DispatcherView, ResearcherView, IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dispatcher/', DispatcherView.as_view(), name='dispatcher'),
    path('researcher/', ResearcherView.as_view(), name='researcher')
]