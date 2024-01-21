from django.urls import path
from . import views

urlpatterns = [
    
path("", views.intial_page, name = 'intial_page'),
path("posts/", views.all_posts, name = 'all_posts'),
path("posts/<slug:slug>", views.post_page, name = 'post_url'),
]
