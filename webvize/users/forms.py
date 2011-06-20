from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

def validate_username(value):
    if User.objects.filter(username=value).exists():
        raise ValidationError(u'%s is already taken' % value)

def validate_email(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError(u'%s is already signed up' % value)

class SignUpForm(forms.Form):
    email = forms.EmailField(validators=[validate_email])
    username = forms.CharField(max_length=40, validators=[validate_username])
    password = forms.CharField( widget=forms.PasswordInput, label="Your Password" )
    password2 = forms.CharField( widget=forms.PasswordInput, label="Re-enter your Password" )
    # http://stackoverflow.com/questions/3226197/why-is-checking-if-two-passwords-match-in-django-so-complicated
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password != password2:
            raise forms.ValidationError("Your passwords do not match")
        return password2
