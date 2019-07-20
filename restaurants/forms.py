from django import forms
from .models import Restaurant
from django.contrib.auth.models import User

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

        widgets = {
        	'opening_time': forms.TimeInput(attrs={'type':'time'}),
        	'closing_time': forms.TimeInput(attrs={'type':'time'}),
        }
class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ['Username','First_name', 'Last_name', 'Email', 'Password']

        widgets={
        'Password': forms.PasswordInput(),
        }
class SigninForm(forms.Form):
    class Meta:
        Username= forms.CharField(required=True)
        Password= forms.CharField(required=True, widget=forms.PasswordInput())
        
