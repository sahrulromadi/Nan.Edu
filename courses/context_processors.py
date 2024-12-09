from courses.models import Course

def courses_count(request):
    if request.user.is_authenticated:
        # Mengambil jumlah kursus yang diakses oleh pengguna yang sedang login
        courses = Course.objects.filter(user_has_access=request.user)
        courses_count = courses.count()
    else:
        courses_count = 0
    
    return {'courses_count': courses_count}