from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from shop.models import*

class RegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=200,required=False)
    last_name=forms.CharField(max_length=200,required=False)
    email=forms.EmailField()


class AddressForm(forms.ModelForm):
    class Meta:
        model=Address
        fields='__all__'
        exclude=('user',)
