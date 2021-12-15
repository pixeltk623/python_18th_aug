from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('course-details/', views.courseDetails, name='courseDetails'),
    path('event/', views.event, name='event'),
    path('pricing/', views.pricing, name='pricing'),
    path('trainers/', views.trainers, name='trainers'),
    path('courses/', views.courses, name='courses'),
]	