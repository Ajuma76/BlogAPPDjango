from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    # first_name = forms.CharField(max_length=100)
    # last_name = forms.CharField(max_length=100)

# gives us a nested namespace for configurations 
# class meta keeps the configurations in one place
# The fields attribute guides the order of appearance of its properties

    class meta: 
        model = User
        fields = ('username','email','password1','password2')


    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'