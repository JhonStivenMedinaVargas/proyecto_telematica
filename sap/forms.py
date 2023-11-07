from django import forms
from .models import CustomUser, Product

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'roles']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description']
