# models.py
from django.db import models

class ContactUs(models.Model):
    STATUS_CHOICES = [
        ('unread', 'Unread'),
        ('read', 'Read'),
    ]
    
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=6,
        choices=STATUS_CHOICES,
        default='unread',
    )

    class Meta:
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return f"Pesan dari {self.name} ({self.email})"
