from django.urls import path
from django.contrib.auth import views
from account import views
urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.logout, name='logout'),
]