from django.urls import path
from . import views

urlpatterns = [
    path('add_user/', views.add_user, name='add_user'),
    path('user_list/', views.user_list, name='user_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('product_list/', views.product_list, name='product_list'),
]
