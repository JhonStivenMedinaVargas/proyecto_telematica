from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserForm, ProductForm
from .models import CustomUser, Product


def index(request):
    return render(request,"index.html")

# # Create your views here.
# def login_sap(request):
    