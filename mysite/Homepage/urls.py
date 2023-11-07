from django.urls import path
from . import views
urlpatterns = [
    path('register', views.registration, name='register'),
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
    path('logout', views.log_out, name='logout'),
]