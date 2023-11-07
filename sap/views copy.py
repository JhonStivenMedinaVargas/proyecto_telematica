from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserForm, ProductForm
from .models import CustomUser, Product




# Create your views here.
def login_sap(request):

    # Crear usuario y guardar en la base de datos.
    user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

    # Actualizar campos y luego guardar nuevamente
    user.first_name = 'John'
    user.last_name = 'Citizen'
    user.save()


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
