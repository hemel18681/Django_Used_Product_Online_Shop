from django import forms
from .models import pending_post

class make_post_form(forms.ModelForm):
    class Meta:
        model = pending_post
        fields = ('post_title', 'post_description', 'post_picture', 'post_bkash','user_phone_number')
        widgets = {
            'post_picture' : forms.FileInput(attrs={'class': 'form-control','default': 'x' }),
            'post_title': forms.TextInput(attrs={'class': 'form-control'}),
            'post_bkash': forms.TextInput(attrs={'class': 'form-control'}),
            'user_phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }