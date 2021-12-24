from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('store/', views.store, name='store'),
    path('register/', views.register, name='register'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.loginReq, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout_view'),
]