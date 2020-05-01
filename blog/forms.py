from django import forms
from blog.models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class UserForm(forms.ModelForm):

    password  = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class UserProfileInfo(forms.ModelForm):
    class Meta():

        model = UserProfileInfo
        fields = ('profile_img','description', 'instagram', 'facebook', 'github')


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','cover_img', 'title', 'text')

        widgets = {
            'title' : forms.TextInput(attrs = {'class' : 'textinputclass'}),
            'text' : SummernoteWidget()
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author' : forms.TextInput(attrs = {'class' : 'textinputclass'}),
            'text' : SummernoteWidget()
        }
