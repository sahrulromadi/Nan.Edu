from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Profile

class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

# Form untuk update foto profil
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo'] 
