from django.db import models


class WorkWithUs(models.Model):
    fullName = models.CharField(max_length=30, verbose_name='نام کامل')
    email = models.EmailField()
    number = models.CharField(max_length=14)
    description = models.TextField()
    cv = models.FileField(upload_to='CV/')
