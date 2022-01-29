from django.contrib import admin
from .models import Course, CourseComment, LikeCourseComment


class CustomCourseCommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'star', 'description', 'is_active']


class CustomCurseAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher', 'price', 'discount', 'label', 'is_active', 'time']


admin.site.register(Course, CustomCurseAdmin)
admin.site.register(CourseComment, CustomCourseCommentAdmin)
admin.site.register(LikeCourseComment)
