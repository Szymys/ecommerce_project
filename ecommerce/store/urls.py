from django.urls import path

from . import views

urlpatterns = [
    
    # STRONA GLOWNA
    path('', views.store, name='store'),

    # KONKRET PRODUKT
    path('product/<slug:product_slug>/', views.product_info, name='product-info'),

    # KATEGORIA
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),



]
