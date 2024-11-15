from django.shortcuts import render, redirect
from .forms import ContactUsForm
from django.contrib import messages

def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, "Form berhasil dikirim!")
            return redirect('contactus') 
        else:
            messages.error(request, "Form gagal dikirim! Pastikan format anda benar!")
    else:
        form = ContactUsForm()

    return render(request, 'contactus.html', {'form': form})
