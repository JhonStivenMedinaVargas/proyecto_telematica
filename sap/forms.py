from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django import forms
from .models import CustomUser, Product

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password', 'roles']
class UserForm(forms.ModelForm):
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Confirmar Contraseña')

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'repeat_password', 'roles']

    ROLES_CHOICES = [
        ('admin', 'Admin'),
        ('lector', 'Lector'),
        ('editor', 'Editor'),
    ]

    roles = forms.ChoiceField(choices=ROLES_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Contraseña')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')

        if password and repeat_password and password != repeat_password:
            raise ValidationError("Las contraseñas no coinciden. Por favor, inténtalo de nuevo.")

        return cleaned_data

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description']

class DeleteProductsForm(forms.Form):
    product_ids = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    def __init__(self, *args, **kwargs):
        products = kwargs.pop('products', None)
        super(DeleteProductsForm, self).__init__(*args, **kwargs)
        if products:
            self.fields['product_ids'].queryset = products
            self.fields['product_ids'].label_from_instance = lambda obj: obj.name


class FormularioLogin(forms.Form):
    usuario = forms.CharField(label="Nombre", required=True,max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Ingrese un usuario'}))
    password = forms.CharField(label="Contraseña",required=True,max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder' : 'Ingrese la contraseña'}))

# class FormularioLogin(AuthenticationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ingrese un usuario'})
#         self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ingrese la contraseña'})