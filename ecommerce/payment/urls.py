
from django.urls import path


from . import views



urlpatterns = [

    # zamowione 
    path('payment-success', views.payment_success, name='payment-success'),

    # blad zamowienia
    path('payment-failed', views.payment_failed, name='payment-failed'),

    # realizacja zamowienia
    path('checkout', views.checkout, name='checkout'),


    path('complete-order', views.complete_order, name='complete-order'),





]































