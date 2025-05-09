from django.urls import path

from django.contrib.auth import views as auth_views

from . import views



urlpatterns = [


 
    path('register', views.register, name='register'),


    # WERYFIKACJA MAILA

    path('email-verification/<str:uidb64>/<str:token>/', views.email_verification, name='email-verification'),


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


# ZMIANA HASLA:

# 1 mail
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="account/password/password-reset.html"), name='reset_password'),

# 2 wyslanie
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="account/password/password-reset-sent.html"), name='password_reset_done'),

# 3 link
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="account/password/password-reset-form.html"), name='password_reset_confirm'),

# 4 sukces
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="account/password/password-reset-complete.html"), name='password_reset_complete'),


# SLEDZENIE ZAMOWIEN
    path('track-orders', views.track_orders, name='track-orders'),



]

