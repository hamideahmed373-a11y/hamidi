from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from.views import *
from .models import *
class OffersForm(ModelForm, forms.Form):
    class Meta:
        model=Offers
        fields='__all__'


class BaseForm(ModelForm, forms.Form):
    class Meta:
        model=Base
        fields='__all__'