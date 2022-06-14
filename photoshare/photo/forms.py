from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self, *arg, **kwargs):
        super(CustomUser,self).__init__(*arg, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Enter username...'})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Enter Email...'})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'confirm password...'})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'confirm password...'})