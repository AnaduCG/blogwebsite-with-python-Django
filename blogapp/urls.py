from django.urls import path
from . import views



urlpatterns = [
    path('',views.homePage, name='home'),
    path('blog/<str:pk>/',views.blogPage, name='blog'),
    path('create/',views.createPost, name='create'),
    path('edit/<str:pk>/',views.editPost, name='edit'),
    path('inbox/',views.inbox, name='inbox'),
    path('message/<str:pk>/',views.message, name='message'),
]
