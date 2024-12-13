from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import Payment
import os

# Menghapus gambar saat Payment dihapus
@receiver(post_delete, sender=Payment)
def delete_payment_proofs_on_Payment_delete(sender, instance, **kwargs):
    if instance.proof_of_payment:  # Gunakan nama field yang benar
        # Menghapus file gambar dari sistem file
        if os.path.isfile(instance.proof_of_payment.path):
            os.remove(instance.proof_of_payment.path)

# Menghapus gambar lama sebelum mengganti dengan gambar baru
@receiver(pre_save, sender=Payment)
def delete_old_payment_proofs_on_Payment_update(sender, instance, **kwargs):
    if instance.pk:  
        try:
            old_instance = Payment.objects.get(pk=instance.pk)
            if old_instance.proof_of_payment and old_instance.proof_of_payment != instance.proof_of_payment:
                # Menghapus file gambar lama jika ada perubahan gambar
                if os.path.isfile(old_instance.proof_of_payment.path):
                    os.remove(old_instance.proof_of_payment.path)
        except Payment.DoesNotExist:
            pass  # Jika objek lama tidak ditemukan, abaikan
