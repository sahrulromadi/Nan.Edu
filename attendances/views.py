from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from datetime import timedelta
from courses.models import Course
from .models import Attendance

@login_required
def mark_attendance(request):
    today = now().date()
    
    # Cek apakah absensi sudah tercatat hari ini
    attendance_exists = Attendance.objects.filter(user=request.user, date=today).exists()

    # Hitung absensi terakhir 7 hari
    last_7_days = Attendance.objects.filter(
        user=request.user,
        date__gte=today - timedelta(days=6)
    ).count()

    if not attendance_exists:
        # Tambahkan absensi untuk hari ini
        Attendance.objects.create(user=request.user)
    
    # Jika user sudah login 7 hari berturut-turut, berikan akses ke course ID 1
    if last_7_days >= 1:
        course = Course.objects.get(id=1)  # Ambil course dengan ID 1
        if not request.user in course.user_has_access.all():
            course.user_has_access.add(request.user)
            course.save()

    return render(request, 'pages/attendances/attendance_view.html', {
        'attendance_exists': attendance_exists,
        'last_7_days': last_7_days,
    })
