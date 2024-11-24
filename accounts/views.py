from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from .models import Profile

@login_required
def profile_update(request):
    # Periksa apakah pengguna memiliki profil. Jika tidak, buat profilnya.
    if not hasattr(request.user, 'profile'):
        request.user.profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        # Membuat form dengan data POST dan file (untuk foto)
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            # Menghapus foto lama sebelum menyimpan jika foto baru ada
            form.save()
            # Setelah berhasil menyimpan, arahkan kembali ke halaman edit profil
            return redirect('edit_profile') 
    else:
        # Jika bukan POST, buat form untuk pengguna yang sudah ada
        form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'form': form,
    }
    return render(request, 'profiles/edit_profile.html', context)
