from django import forms
from django.core.exceptions import ValidationError
from .models import Registration
from django.core import validators

# def clean_name(name):
#     if len(name) <= 4:
#         print("yes validation raising character counting")
#         raise ValidationError('Name must be at least 4 characters long.')

def clean_Email(Email):            
    if(Email is not None):    
        if('.' not in Email):
            print('Missing "." in Email id')
            raise ValidationError('Missing "." in Email id')
        
        if('@' not in Email):
            print('Missing "@" in Email id')
            raise ValidationError('Missing "@" in Email id')
        
# def clean_Password(password):            
#     if(password is not None):    
#         if('.' not in password):
#             print('Missing "." in Email id')
#             raise ValidationError('Missing "." in Email id')
        
#         if('@' not in password):
#             print('Missing "@" in Email id')
#             raise ValidationError('Missing "@" in Email id')
        
class UserForm(forms.ModelForm):
    first_name = forms.CharField(validators=[validators.MinLengthValidator(4, "Name must be at least 4 characters long.")], widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 200px;'}))
    last_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'width: 200px;'}))
    Email = forms.EmailField(validators=[clean_Email], widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 200px;'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'style': 'width: 200px;'}))  

    # def clean_Email(self):   
    #     Email = self.cleaned_data.get("Email")         
    #     if(Email is not None):    
    #         if('.' not in Email):
    #             print('Missing "." in Email id')
    #             raise ValidationError('Missing "." in Email id')
            
    #         if('@' not in Email):
    #             print('Missing "@" in Email id')
    #             raise ValidationError('Missing "@" in Email id')
            
    class Meta:
        model = Registration
        fields = "__all__"

    labels = {
        "first_name": "First Name",  # for displaying exact name
        "last_name": "Last Name",
        "Email": "E-mail",
        "password": "Password",
    }



class LoginForm(forms.ModelForm):
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 200px;'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'style': 'width: 200px;'}))


    class Meta:
        model = Registration
        fields = ['Email', 'password']
        
        labels = {
            "Email": "E-mail",
            "password": "Password",
        }