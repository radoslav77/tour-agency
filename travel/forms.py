from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView

from .models import *


class registrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

class PostForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title','user','price','text','from_date','to_date','image')

class SearchForm(forms.ModelForm):
     
     
    class Meta:
        model = Search
        fields = ('Choose_country','When_would_you_travel','How_many_people')

class BookingForm(forms.Form):
    holiday  = forms.CharField(label='Holiday packedge', max_length=100)
    date = forms.DateField(label='date from')
    end = forms.DateField(label='date to')
    people = forms.IntegerField(label='people')