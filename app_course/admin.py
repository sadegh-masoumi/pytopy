from django.contrib import admin
from .models import Course, CourseComment, LikeCourseComment, Episode, Season, UserDownloadEpisode


class CustomCourseCommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'star', 'description', 'is_active']


class CustomCurseAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher', 'price', 'discount', 'label', 'is_active', 'time']


admin.site.register(Course, CustomCurseAdmin)
admin.site.register(CourseComment, CustomCourseCommentAdmin)
admin.site.register(LikeCourseComment)


class CustomEpisodeAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'season', 'path', 'is_free', 'is_active']


admin.site.register(Episode, CustomEpisodeAdmin)


class CustomSeasonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'number']


admin.site.register(Season, CustomSeasonAdmin)


class CustomUserDownloadEpisodeAdmin(admin.ModelAdmin):
    list_display = ['episode', 'user', 'count']


admin.site.register(UserDownloadEpisode, CustomUserDownloadEpisodeAdmin)
