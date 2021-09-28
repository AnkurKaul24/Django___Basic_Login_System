from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from django import forms


class userRegistrationForm(UserCreationForm):

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta:

        model = User

        fields = ['first_name','last_name','username','email','password1','password2']


class userUpdateForm(forms.ModelForm):

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta:

        model = User

        fields = ['first_name','last_name','username','email']