from django.urls import path
from .import views

urlpatterns = [

    # BackEnd start Urls #
    path('dashboard', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),

    # BackEnd End Urls #

    # FrontEnd start Urls #
    path('', views.main, name='main'),
    # FrontEnd start Urls #
]
