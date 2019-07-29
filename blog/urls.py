from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list , name='post_list'),
    path('new/', views.post_new, name= 'post_new'),
    path('<int:pk>/',views.post_detail, name='post_detail'),
    path('<int:pk>/edit',views.post_edit, name='post_edit'),
    path('<int:pk>/',views.post_remove, name='post_remove'),
    path('<int:pk>/published',views.post_publish, name='post_publish'),
    path('<tags>/', views.post_tags, name='post_tags'),
]