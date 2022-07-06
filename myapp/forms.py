from django import forms
from .models import Post
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'thumbnail')

    def __init__(self, *args, **kwrgs):
        super().__init__(*args, **kwrgs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwrgs):
        super().__init__(*args, **kwrgs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class SignUpForm(UserCreationForm):
     class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

     def __init__(self, *args, **kwrgs):
        super().__init__(*args, **kwrgs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
