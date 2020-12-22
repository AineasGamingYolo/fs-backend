from .models import Comment, CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
'''
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = '__all__'
'''