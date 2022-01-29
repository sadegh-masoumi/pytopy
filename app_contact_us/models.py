from django.db import models


class Contact(models.Model):
    fullName = models.CharField(max_length=30)
    email = models.EmailField()
    number = models.CharField(max_length=14)
    title = models.CharField(max_length=30)
    message = models.TextField()

    observed = models.BooleanField(default=False)

    def __str__(self):
        return self.fullName
