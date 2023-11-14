import json
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required

import requests
from .forms import FormularioLogin, UserForm, ProductForm,DeleteProductsForm
from .models import CustomUser, Product

def index(request):
    return render(request,"index.html")


def login(request):
    form = FormularioLogin()
    context = {"type": "", "mensaje": ""}
    if request.method == "POST":

        print("entreee mor ")
        user = request.POST.get("usuario")
        password = request.POST.get("password")
        print(f'user: {user}, pass: {password}')
        user1 = authenticate(request, username=user, password=password)
        print(user1)
        try:
            usuarios = CustomUser.objects.get(username= user)
        #for usuario in usuarios:
        #    print(f'ID: {usuario.id}, Usuario: {usuario.username}, Roles: {usuario.roles}, Password: {usuario.password}')
            print(f'usuarios: {usuarios.roles}, llega {type(password)}')
            if password in usuarios.password:
                # si la clave es valida hace login 

                print("login correcto")
                request.session.set_expiry(0)  # Opcional: cerrar sesión al cerrar el navegador
                request.session.save()
                request.session["username"] = usuarios.username
                request.session["rol"] = usuarios.roles
                # session["token"] = response_api["token"]
                # session["rol"] = response_user["rol"]
                # session["username"] = username
                return redirect('home')
            else:
                print("Fallo en la autenticación")
                return render(request, "login.html", {'form':form, 'error':'Usuario o contraseña incorrecta'})
       
        except CustomUser.DoesNotExist:
            print('entra el except')
            return render(request, "login.html", {'form':form, 'error':'Usuario o contraseña incorrecta'})
    logout(request)
    return render(request,"login.html", {'form':form})


# # Create your views here.
# def login_sap(request):

def login_view(request):
    if request.method == 'POST':
        form = FormularioLogin(request, request.POST)
        print('Formulario')
        if form.is_valid():
            print('formulario valido')
            usuario = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=usuario, password=password)
            print(f'user: {user}')
            if user is not None:
                login(request, user)
                # Redirige a la vista según el rol del usuario
                return redirect('home')  # Ajusta 'home' según tus necesidades
            else:
                # Manejar el caso en que la autenticación falla
                return render(request, 'new_login.html', {'form': form, 'error_message': 'Usuario o contraseña incorrectos'})
    else:
        form = FormularioLogin()

    return render(request, 'new_login.html', {'form': form})

#@login_required
def home(request):
    rol = request.session.get('rol', None)
    print('entra al home',rol)

    if rol == 'admin':
        return render(request,'index.html')
    elif rol == 'lector':
        products = Product.objects.all()
        return render(request, 'product_list.html', {'products': products})
    elif rol == 'editor':
        products = Product.objects.all()
        return render(request, 'product_list.html', {'products': products})
    else:
        return render(request, 'index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def delete_products(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = DeleteProductsForm(request.POST, products=products)
        if form.is_valid():
            # Manejar la lógica de eliminación aquí
            product_ids_to_delete = form.cleaned_data['product_ids']
            Product.objects.filter(pk__in=product_ids_to_delete).delete()
            return redirect('product_list')
    else:
        form = DeleteProductsForm(products=products)

    return render(request, 'delete_products.html', {'form': form})

def logout_sesion(request):
    logout(request)
    return redirect('login')
