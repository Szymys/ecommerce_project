from django.urls import path



from . import views

urlpatterns = [


 
    path('register', views.register, name='register'),


    # WERYFIKACJA MAILA

    path('email-verification', views.email_verification, name='email-verification'),


    path('email-verification-sent', views.email_verification_sent, name='email-verification-sent'),


    path('email-verification-success', views.email_verification_success, name='email-verification-success'),


    path('email-verification-failed', views.email_verification_failed, name='email-verification-failed'),



# LOGOWANIE 

    path('my-login', views.my_login, name='my-login'),


# WYLOGOWANIE

    path('user-logout', views.user_logout, name='user-logout'),


# PANEL
    path('dashboard', views.dashboard, name='dashboard'),


# ZARZADZANIE KONTEM
    path('profile-management', views.profile_management, name='profile-management'),


# USUWANIE KONTA
    path('delete-account', views.delete_account, name='delete-account'),


# KUPOWANIE
    path('manage-shipping', views.manage_shipping, name='manage-shipping'),



]

