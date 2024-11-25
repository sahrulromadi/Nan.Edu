from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, ProfileForm
from .models import Profile

@login_required
def profile_view(request):
    # Ambil profil pengguna (jika sudah ada)
    profile = getattr(request.user, 'profile', None)

    # Jika profil tidak ada, buat profil baru
    if profile is None:
        profile = Profile.objects.create(user=request.user)

    context = {
        'user': request.user,  # Data pengguna
        'profile': profile,    # Data profil (termasuk foto profil)
    }
    return render(request, 'view_profile.html', context)

def profile_update(request):
    # Periksa apakah pengguna memiliki profil. Jika tidak, buat profilnya.
    if not hasattr(request.user, 'profile'):
        request.user.profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        # Membuat form untuk pengguna dan profil (termasuk foto profil)
        user_form = ProfileUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            # Simpan perubahan user
            user_form.save()
            # Simpan perubahan profil (foto)
            profile_form.save()
            return redirect('edit_profile') 
    else:
        # Jika bukan POST, buat form dengan data pengguna dan profil yang ada
        user_form = ProfileUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'edit_profile.html', context)
