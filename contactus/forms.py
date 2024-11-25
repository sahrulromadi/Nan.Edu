# forms.py
from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'phone', 'email', 'message']
        
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
