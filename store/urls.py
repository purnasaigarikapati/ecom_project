from django.urls import path

from . import views


urlpatterns = [

path('', views.home, name='home'),

path('register/', views.register, name='register'),

path('login/', views.login_view, name='login'),

path('logout/', views.logout_view, name='logout'),

path('products/', views.product_list, name='products'),

path('cart/', views.cart, name='cart'),

path('orders/', views.orders, name='orders'),

]