from django.shortcuts import render, redirect
from .forms import ContactUsForm

def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()  # Menyimpan data ke database
            return redirect('home')  # Arahkan ke halaman 
        else:
            # Form tidak valid, tampilkan kembali dengan error
            print(form.errors)
    else:
        form = ContactUsForm()

    return render(request, 'contactus.html', {'form': form})
