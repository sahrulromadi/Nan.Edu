from django.shortcuts import render, redirect
from .forms import ContactUsForm
from django.contrib import messages

def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Pesan berhasil dikirim!', extra_tags='contactus')
            return redirect('contactus') 
        else:
            messages.error(request, 'Terjadi kesalahan.', extra_tags='contactus')
    else:
        form = ContactUsForm()

    return render(request, 'contactus.html', {'form': form})
