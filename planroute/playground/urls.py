from django.urls import path
from .views import show_posts

urlpatterns = [
    path('playground/', show_posts, name='playground'),
]