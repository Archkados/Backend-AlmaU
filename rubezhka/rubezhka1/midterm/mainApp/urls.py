from django.urls import path
from mainApp import views

urlpatterns = [
    path('/api/blogs', views.blog_list_handler),
    path('/api/blogs/<int:pk>', views.blog_list_handler),
]