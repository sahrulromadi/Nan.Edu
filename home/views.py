from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from datetime import timedelta
from courses.models import Course
from .models import Attendance
from news.models import News
from courses.models import Course

# Home view
def home(request):
    latest_news = News.objects.order_by('-created_at')[:5]
    latest_courses = Course.objects.order_by('-created_at')[:5]

    # Absensi logic
    attendance_exists = False
    last_7_days = 0
    remaining_days_for_access = 0
    attendance_range = list(range(7))

    show_modal = True # modal agar hanya tampil 1 kali

    if request.user.is_authenticated:
        today = now().date()
        
        # Cek apakah absensi sudah tercatat hari ini
        attendance_exists = Attendance.objects.filter(user=request.user, date=today).exists()

        # Hitung absensi terakhir 7 hari
        last_7_days = Attendance.objects.filter(
            user=request.user,
            date__gte=today - timedelta(days=6)
        ).count()

        # Menghitung sisa hari untuk mencapai 7 hari login berturut-turut
        remaining_days_for_access = max(0, 7 - last_7_days)

        # Menambahkan absensi jika belum tercatat
        if not attendance_exists:
            Attendance.objects.create(user=request.user)

        # Jika user sudah login 7 hari berturut-turut, berikan akses ke course ID 1
        if last_7_days >= 1:
            try:
                course = Course.objects.get(id=1)  # Ambil course dengan ID 1
                if not request.user in course.user_has_access.all():
                    course.user_has_access.add(request.user)
                    course.save()
            except Course.DoesNotExist:
                # Tangani jika course dengan ID 1 tidak ditemukan
                print("Course with ID 1 does not exist.")

    context = {
        'latest_news': latest_news,
        'latest_courses': latest_courses,
        'attendance_exists': attendance_exists,
        'last_7_days': last_7_days,
        'attendance_range': attendance_range,
        'remaining_days_for_access': remaining_days_for_access,
        'show_modal': show_modal,
    }
    return render(request, 'pages/home/home.html', context)
