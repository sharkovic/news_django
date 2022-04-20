from django import forms
from .models import Post, User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title_post', 'text_post', 'category', 'rating_post', 'author']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']