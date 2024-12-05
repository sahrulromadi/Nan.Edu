from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import CourseContent, Course
import os

# Menghapus gambar saat CourseContent dihapus
@receiver(post_delete, sender=Course)
def delete_image_on_course_delete(sender, instance, **kwargs):
    if instance.image:  # Pastikan ada gambar yang terkait
        # Menghapus file gambar dari sistem file
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

# Menghapus gambar lama sebelum mengganti dengan gambar baru
@receiver(pre_save, sender=Course)
def delete_old_image_on_course_update(sender, instance, **kwargs):
    if instance.pk:  # Jika ini adalah update, bukan create
        old_instance = Course.objects.get(pk=instance.pk)
        if old_instance.image != instance.image:
            # Menghapus file gambar lama jika ada perubahan gambar
            if old_instance.image:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)

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

