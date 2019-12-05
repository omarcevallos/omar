from django import forms
from django.contrib.auth.models import User
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = (
				'first_name',
				'last_name',
				'username',
				'email',
                'password',
                'groups'
				)
