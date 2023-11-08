from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(label="Логин")
    password = forms.CharField(widget=forms.PasswordInput)


class MyPasswordChangeForm(PasswordChangeForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'passInput', 'placeholder': 'Email address', }))

    class Meta:
        fields = ['email']


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Логин")
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Этот Email уже используется')
        return data


class ProfileEditForm(forms.ModelForm):
    photo = forms.ImageField(label="",
                             help_text="Можете выбрать свое фото",
                             required=False,
                             )

    class Meta:
        model = Profile
        fields = ['photo']
