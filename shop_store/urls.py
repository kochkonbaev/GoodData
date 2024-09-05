from django.urls import path
from .views import *
urlpatterns = [
    path('index.html', index, name='index'),
    path('contact.html', contact_us, name='contact'),
    path('about.html', about_us, name='about')

]