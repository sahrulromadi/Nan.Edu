# forms.py
from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'phone', 'email', 'message']
        # custom field
        widgets = {
            'name': forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Name*',
                'required' : True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Phone*', 
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Email*', 
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Message*', 
                'rows': 6, 
                'required': True
            }),
        }
        # custom error message
        error_messages = {
            'name': {
                'required': "Nama tidak boleh kosong.",
                'max_length': "Nama terlalu panjang.",
            },
            'phone': {
                'required': "Nomor telepon harus diisi.",
                'invalid' : 'Nomor telepon harus diisi dengan angka'
            },
            'email': {
                'required': "Email harus diisi.",
                'invalid': "Format email tidak valid.",
            },
            'message': {
                'required': "Pesan tidak boleh kosong.",
            }
        }
