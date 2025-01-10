from django.urls import path



from . import views

urlpatterns = [


 
    path('register', views.register, name='register'),


    # WERYFIKACJA MAILA

    path('email-verification', views.email_verification, name='email-verification'),


    path('email-verification-sent', views.email_verification_sent, name='email-verification-sent'),


    path('email-verification-success', views.email_verification_success, name='email-verification-success'),


    path('email-verification-failed', views.email_verification_failed, name='email-verification-failed'),



# LOGOWANIE I WYLOGOWANIE

    path('my-login', views.my_login, name='my-login'),


# WYLOGOWANIE

    # path()


# PANEL
    path('dashboard', views.dashboard, name='dashboard')




]

