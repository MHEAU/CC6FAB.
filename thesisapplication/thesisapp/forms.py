from django.forms import ModelForm
from django import forms
from .models import Thesis
from .models import thesisapp_comments
from django.forms.widgets import DateInput
from django.contrib.auth.models import User, auth

class ThesisForm(ModelForm):
    class Meta:
        model = Thesis
        fields = ('callno', 'title', 'authors', 'adviser', 'abstract', 'sub_date', 'college', 'program',)
        widgets = {
            'sub_date': DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
        }
        
class CommentForm(ModelForm):
    class Meta:
        model = thesisapp_comments
        fields = ('id', 'content')

from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Incorrect username or password")

        return cleaned_data
