from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    email = forms.CharField(required=True, label='Email')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)
    next = forms.CharField(required=False, widget=forms.HiddenInput)


class CustomUserCreationForm(forms.ModelForm):
    email = forms.CharField(label='Email', required=True)
    phone = forms.CharField(label='Телефон', required=True)
    first_name = forms.CharField(label='Имя', required=True)
    last_name = forms.CharField(label='Фамилия', required=False)
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвердите пароль', strip=False, required=True, widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('is_worker', 'email', 'password', 'password_confirm', 'phone', 'first_name', 'last_name', 'avatar', 'birthday')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Пароли не совпадают')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))

        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'avatar', 'phone', 'birthday')
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email', 'avatar': '', 'phone': 'Телефон', 'birthday': 'День рождения'}
