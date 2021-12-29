from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('payment/', views.paymentForm, name='paymentForm'),
    path('charge/', views.chargePayment, name='chargePayment'),
]