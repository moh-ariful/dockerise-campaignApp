from django.db import models

# Create your models here.
class Kampanye(models.Model):
    nama = models.CharField(max_length=21)
    konten = models.TextField(max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nama
