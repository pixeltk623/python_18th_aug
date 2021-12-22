from django.db import models

# Create your models here.


class FileUpload(models.Model):
    name = models.CharField(max_length=255)
    file = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
