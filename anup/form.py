from django import forms
from .models import User


class UserForm(forms.ModelForm):


    Status = forms.CharField(max_length=120)

    class  Meta:
        model=User


        fields=['username','password','first_name','last_name','email','birth_date','address','Status']


class RoleForm(forms.ModelForm):

    class Meta:
        fields=['username','first_name','email','role']
