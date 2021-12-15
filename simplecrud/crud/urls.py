from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('store/', views.store, name='store'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('show/<int:id>/', views.show, name='show'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/', views.update, name='update'),
]