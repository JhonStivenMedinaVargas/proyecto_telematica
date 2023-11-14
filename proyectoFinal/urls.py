"""proyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from sap.views import login, login_view,home,logout_sesion,product_list,add_user,add_product,delete_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login,name='login'),
    path('home/', home, name='home'),
    path('product_list/', product_list, name='product_list'),
    path('add_user/', add_user, name='add_user'),
    path('add_product/', add_product, name='add_product'),
    path('delete_product/', delete_products, name='delete_product'),
    path('logout/', logout_sesion, name='logout'),
    #path('', include('sap.urls')),
]
