from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
