from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=4, max_length=10, widget=forms.TextInput(attrs={"type": "password"}))


class RegistrationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=4, max_length=10, widget=forms.TextInput(attrs={"type": "password"}))
    birth_date = forms.DateField()
    photo = forms.FileField()
