from django.contrib.auth import get_user_model
from django import forms


class ContactForm(forms.Form):
    fullName = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '20'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )


class LoginForm(forms.Form):
    userName = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter your password'})
    )


User = get_user_model()


class RegisterForm(forms.Form):
    userName = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your username'})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter your password'})
    )
    confirmPassword = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 're-enter your password'})
    )

    def clean_userName(self):
        userName = self.cleaned_data.get('userName')
        query = User.objects.filter(username=userName)
        if query.exists():
            raise forms.ValidationError('this username is not available')
        return userName

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "gmail.com" in email:
            raise forms.ValidationError('email has to be gmail.com')

        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        confirmpassword = self.cleaned_data.get('confirmPassword')

        if password != confirmpassword:
            raise forms.ValidationError('passwords do not match')

        return data
