from django.urls import path
from .views import index, contact, about, resume_view

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('resume/', resume_view, name='resume'),
    ]

