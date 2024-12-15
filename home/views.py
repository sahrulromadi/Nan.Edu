from django.shortcuts import render
from django.utils.timezone import localtime, now
from datetime import timedelta
from courses.models import Course
from .models import Attendance
from news.models import News

def home(request):
    latest_news = News.objects.order_by('-created_at')[:5]
    latest_courses = Course.objects.order_by('-created_at')[:5]

    attendance_exists = False
    last_7_days = 0
    remaining_days_for_access = 0
    attendance_range = list(range(7))
    accessible_course = None
    show_modal = False

    if request.user.is_authenticated:
        today = localtime(now()).date()

        # Gunakan get_or_create untuk membuat absensi hanya jika belum ada
        attendance, created = Attendance.objects.get_or_create(
            user=request.user,
            date=today
        )
        attendance_exists = not created  # Jika created=False, berarti sudah ada

        # Hitung absensi selama 7 hari terakhir
        last_7_days = Attendance.objects.filter(
            user=request.user,
            date__gte=today - timedelta(days=6)
        ).count()

        # Hitung sisa hari untuk akses
        remaining_days_for_access = max(0, 7 - last_7_days)

        # Berikan akses ke course jika absensi selama 7 hari berturut-turut
        if last_7_days >= 7:
            try:
                accessible_course = Course.objects.get(id=1)
                if request.user not in accessible_course.user_has_access.all():
                    accessible_course.user_has_access.add(request.user)
                    accessible_course.save()
            except Course.DoesNotExist:
                accessible_course = None

        # Tentukan apakah modal ditampilkan
        if last_7_days <= 7 and not request.session.get('modal_shown', False):
            show_modal = True
            request.session['modal_shown'] = True
        elif last_7_days > 7:
            request.session['modal_shown'] = False

    context = {
        'latest_news': latest_news,
        'latest_courses': latest_courses,
        'attendance_exists': attendance_exists,
        'last_7_days': last_7_days,
        'attendance_range': attendance_range,
        'remaining_days_for_access': remaining_days_for_access,
        'show_modal': show_modal,
        'accessible_course': accessible_course,
    }
    return render(request, 'pages/home/home.html', context)
