from django.urls import path
from django.contrib.auth.views import login, logout

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('leader/', views.LeaderView.as_view(), name='leader'),
    path('worker/', views.WorkerView.as_view(), name='worker')
]