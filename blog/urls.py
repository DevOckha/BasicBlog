from django.urls import path
from .views import home, about, posts, post, sendEmail

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('posts/', posts, name='posts'),
    path('post/<slug:slug>/', post, name='post'),

    path('send_email/', sendEmail, name='send_email'),
]