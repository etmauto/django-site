from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about),
    path('contact', views.contact, name='contact'),
    path('career', views.career, name='career'),
    path('home', views.home, name='home'),
]
