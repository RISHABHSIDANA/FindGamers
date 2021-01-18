from django.contrib import admin
from django.urls import path
from gamers import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('pubg',views.pubg,name='pubg'),
    path('services',views.services,name='services'),
    path('matching',views.matching,name='matching')
]