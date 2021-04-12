from django import forms
from .models import pending_post

class make_post_form(forms.ModelForm):
    class Meta:
        model = pending_post
        fields = ('post_title', 'post_description', 'post_picture','post_used_days', 'post_money','user_phone_number')
        widgets = {
            'post_picture' : forms.FileInput(attrs={'class': 'form-control','default': 'x' }),
            'post_title': forms.TextInput(attrs={'class': 'form-control'}),
            'post_money': forms.TextInput(attrs={'class': 'form-control'}),
            'post_used_days': forms.TextInput(attrs={'class': 'form-control'}),
            'user_phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            
        }