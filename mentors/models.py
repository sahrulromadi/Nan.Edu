from django.db import models

class Mentor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='mentor_photos/', blank=True, null=True)
    linked_in = models.URLField(blank=False, null=False)  
    instagram = models.URLField(blank=False, null=False)  
    experience = models.TextField(blank=False, null=False) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name
