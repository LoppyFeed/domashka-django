from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('reviews/', views.reviews, name='reviews'),
]
