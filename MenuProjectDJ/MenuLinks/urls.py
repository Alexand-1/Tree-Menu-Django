from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/programming/', views.programming, name='programming'),
    path('services/programming/design/', views.design, name='design'),
    path('services/advertising/', views.advertising, name='advertising'),
    path('products/', views.products, name = 'prosucts'),
    path('products/product-a/', views.product_a, name='product_a'),
    path('products/product-b/', views.product_b, name='product_b'),
    path('contact/', views.contact, name='contact'),
    path('services/programming/web-development/', views.web_development, name='web-development'),
]