# views.py
from django.shortcuts import render
from mentors.models import Mentor

def aboutus(request):
    # Data FAQ
    faq = [
        {
            'q': 'Apakah kelas ini dapat diikuti oleh semua kalangan?',
            'a': 'Kelas ini dapat diikuti oleh semua kalangan, mulai dari remaja hingga orangtua. Tanpa memiliki batasan usia.'
        },
        {
            'q': 'Apa manfaat dari mengikuti kelas ini?',
            'a': 'Dengan mengikuti kelas ini, Anda akan mendapat pengetahuan dan wawasan mengenai ilmu mengatur keuangan serta strategi untuk mengatur keuangan pribadi atau bisnis.'
        },
        {
            'q': 'Berapa lama durasi dalam 1 kelas?',
            'a': 'Durasi kelas yang kami sediakan memiliki rentan waktu 1-3 bulan.'
        },
        {
            'q': 'Bagaimana proses pembelajaran dilakukan?',
            'a': 'Proses pembelajaran dilakukan secara online.'
        },
    ]
    
    mentors = Mentor.objects.all()

    return render(request, 'aboutus.html', {'faq': faq, 'mentors': mentors})