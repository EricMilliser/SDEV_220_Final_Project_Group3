from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Item, Order

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'isAvailable']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['item', 'quantity']
