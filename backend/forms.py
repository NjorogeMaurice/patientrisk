from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation


class FileUploadForm(forms.Form):
    file = forms.FileField(label='file',widget=forms.FileInput(attrs={'class':'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50  focus:outline-none','aria-describedby':'file_input_help','required':'true','id':'fileInput'}))

class CustomSignupForm(forms.Form):
    email = forms.EmailField(label='Email' ,widget=forms.EmailInput(attrs={'class': 'border placeholder-gray-400 focus:outline-none focus:border-black w-full pt-4 pr-4 pb-4 pl-4 mt-2 mr-0 mb-0 ml-0 text-base block bg-white border-gray-300 rounded-md','required':'true'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'border placeholder-gray-400 focus:outline-none focus:border-black w-full pt-4 pr-4 pb-4 pl-4 mt-2 mr-0 mb-0 ml-0 text-base block bg-white border-gray-300 rounded-md','required':'true'}))

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Validate the password using Django's built-in validators
        try:
            password_validation.validate_password(password)
        except forms.ValidationError as error:
            self.add_error('password', error)
        return password
    

class CustomSigninForm(forms.Form):
    email = forms.EmailField(label='Email' ,widget=forms.EmailInput(attrs={'class': 'border placeholder-gray-400 focus:outline-none focus:border-black w-full pt-4 pr-4 pb-4 pl-4 mt-2 mr-0 mb-0 ml-0 text-base block bg-white border-gray-300 rounded-md','required':'true'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'border placeholder-gray-400 focus:outline-none focus:border-black w-full pt-4 pr-4 pb-4 pl-4 mt-2 mr-0 mb-0 ml-0 text-base block bg-white border-gray-300 rounded-md','required':'true'}))

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Validate the password using Django's built-in validators
        try:
            password_validation.validate_password(password)
        except forms.ValidationError as error:
            self.add_error('password', error)
        return password
