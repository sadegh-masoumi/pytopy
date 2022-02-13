from django.db import models

from app_course.models import Course
from app_user.models import User


class Enroll(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    course = models.ForeignKey(Course, models.CASCADE)

    create_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_pay = models.BooleanField(default=False)

    token = models.CharField(max_length=30)

    amount = models.IntegerField(verbose_name='مبلغ پرداخت شده به تومان')

    def __str__(self):
        return f"{self.user}"
