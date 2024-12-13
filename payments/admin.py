from django.contrib import admin
from django.utils.html import format_html
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'amount', 'status', 'proof_preview', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'course__title')
    actions = ['accept_payments', 'reject_payments']
    readonly_fields = ('user', 'course', 'amount', 'proof_of_payment', 'created_at', 'proof_preview')
    
    fieldsets = (
        (None, {
            'fields': ('user', 'course', 'amount', 'proof_preview', 'status', 'created_at')
        }),
    )

    def proof_preview(self, obj):
        """Menampilkan pratinjau bukti pembayaran."""
        if obj.proof_of_payment:
            return format_html(
                '<a href="{}" target="_blank"><img src="{}" style="max-height: 100px;"/></a>',
                obj.proof_of_payment.url,
                obj.proof_of_payment.url
            )
        return "No proof uploaded"

    proof_preview.short_description = 'Proof of Payment'

    def get_readonly_fields(self, request, obj=None):
        """Membatasi field yang dapat diedit."""
        if obj:
            return self.readonly_fields + ('status',) if obj.status != 'PENDING' else self.readonly_fields
        return self.readonly_fields

    def accept_payments(self, request, queryset):
        """Aksi untuk menerima pembayaran."""
        updated = 0
        for payment in queryset:
            if payment.status != Payment.PaymentStatus.ACCEPTED:
                payment.status = Payment.PaymentStatus.ACCEPTED
                payment.save()
                payment.course.user_has_access.add(payment.user)  # Berikan akses ke kursus
                updated += 1
        self.message_user(request, f'{updated} payments accepted and access granted.')

    def reject_payments(self, request, queryset):
        """Aksi untuk menolak pembayaran."""
        updated = 0
        for payment in queryset:
            if payment.status != Payment.PaymentStatus.REJECTED:
                payment.status = Payment.PaymentStatus.REJECTED
                payment.save()
                # Hapus akses pengguna jika sebelumnya diterima
                if payment.course.user_has_access.filter(id=payment.user.id).exists():
                    payment.course.user_has_access.remove(payment.user)
                updated += 1
        self.message_user(request, f'{updated} payments rejected and access revoked.')

    def save_model(self, request, obj, form, change):
        """Memastikan akses dihapus saat status diubah ke REJECTED atau PENDING."""
        if change:  # Jika sedang mengupdate
            old_obj = Payment.objects.get(pk=obj.pk)
            if old_obj.status == Payment.PaymentStatus.ACCEPTED and obj.status in [
                Payment.PaymentStatus.REJECTED,
                Payment.PaymentStatus.PENDING,
            ]:
                # Hapus akses jika status berubah dari ACCEPTED
                obj.course.user_has_access.remove(obj.user)
        super().save_model(request, obj, form, change)

    accept_payments.short_description = 'Accept selected payments'
    reject_payments.short_description = 'Reject selected payments'
