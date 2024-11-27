from django.db import models

class Mentor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='mentor_photos/', blank=True, null=True)
    linked_in = models.URLField(blank=True, null=True)  
    instagram = models.URLField(blank=True, null=True)  
    experience = models.TextField(blank=True, null=True)  

    def __str__(self):
        return self.name
