from django import forms
from .models import user_info

class uploadformuserpic_post(forms.ModelForm):
    class Meta:
        model = user_info
        fields = ('user_name', 'user_phone_number', 'user_mail', 'user_picture', 'user_password')


class uploadformuserpic_get(forms.ModelForm):
    class Meta:
        model = user_info
        fields = ('user_picture', 'user_password')
        widgets = {
            'user_password' : forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}),
            'user_picture' : forms.FileInput(attrs={'class': 'form-control','default': 'x' }),
        }
