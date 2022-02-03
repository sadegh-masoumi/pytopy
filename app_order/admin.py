from django.contrib import admin
from .models import Enroll


class CustomEnrolAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'is_active', 'is_pay']
    list_filter = ['is_pay']


admin.site.register(Enroll, CustomEnrolAdmin)
