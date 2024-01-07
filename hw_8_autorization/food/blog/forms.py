from django import forms
from .models import News, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.Form):
    title = forms.CharField(max_length=50, label='Заголовок новости: ')
    content = forms.CharField(widget=forms.Textarea, label='Содержание')
    username = forms.CharField(max_length=20, label='Логин')
    last_name = forms.CharField(max_length=20, label='Фамилия')
    first_name = forms.CharField(max_length=20, label='Имя')
    email = forms.EmailField(max_length=50, label='email')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['news', 'published_at']

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'last_name', 'first_name', 'password1', 'password2')

