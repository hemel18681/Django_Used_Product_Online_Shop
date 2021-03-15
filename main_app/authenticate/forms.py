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
        
