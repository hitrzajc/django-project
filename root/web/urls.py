from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    #path('', 'web.urls'),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    #path('logout/', views.user_logout, name='logout'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('settings/', views.user_settings, name='settings'),
    path('match/', views.match, name='match'),
]
