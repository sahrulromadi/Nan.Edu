from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import CourseContent

@receiver(post_delete, sender=CourseContent)
def update_order_after_delete(sender, instance, **kwargs):
    # Setelah konten dihapus, urutkan kembali konten di kursus yang sama
    reorder_contents(instance.course)

def reorder_contents(course):
    # Ambil semua konten dari kursus yang diurutkan berdasarkan 'order'
    contents = CourseContent.objects.filter(course=course).order_by('order')
    
    # Update urutan konten agar tetap berurutan
    for index, content in enumerate(contents):
        content.order = index + 1  # Mulai dari 1
        content.save()

