from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import widgets

from users.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ["username", "password"]


username = forms.CharField()
password = forms.CharField()

#     label="Пароль",
#     widget=forms.PasswordInput(
#         attrs={
#             "autocomplete": "current-password",
#             "class": "form-control",
#             "placeholder": "Введите ваш пароль",
#         }
#     ),
# )

# username = forms.CharField(
#     label="Имя",
#     widget=forms.TextInput(
#         attrs={
#             "autofocus": True,
#             "class": "form-control",
#             "placeholder": "Введите ваше имя пользователя",
#         }
#     ),
# )
# password = forms.CharField(
#     label="Пароль",
#     widget=forms.PasswordInput(
#         attrs={
#             "autocomplete": "current-password",
#             "class": "form-control",
#             "placeholder": "Введите ваш пароль",
#         }
#     ),
# )
