from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from django import forms
from .models import User


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))

    class Meta(UserCreationForm):
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email ID'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone', "maxlength": "10"}),

        }


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': ' ', 'placeholder': 'Email Id'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': ' ', 'placeholder': 'Password', }))


# edit Personal Details
class EditUserForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name '}),
            'last_name': forms.TextInput(attrs={'placeholder': 'last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'phone'})
        }


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Old Password'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'New Password '}))
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm new password '}))




class UserValidate(forms.Form):
    email = forms.CharField(label='Email',widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    phone = forms.CharField(label='Phone Number',widget=forms.TextInput(attrs={'placeholder':'Phone number',"maxlength": "10"}))

class ForgotPasswordForm(SetPasswordForm):
    email = forms.CharField(label='Email',widget=forms.EmailInput(attrs={'placeholder':'Email',"readonly": "True"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"maxlength": "10","readonly": "True"}))
    new_password1= forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    new_password2= forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs={'placeholder':'confirm password'}))

    field_order = ['email', 'phone', 'new_password1','new_password2']
 