from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username', 'number', 'image'
                           , 'first_name', 'last_name', 'date_joined'
                           )}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'username', 'number', 'image', 'is_staff', 'is_active'
                       , 'first_name', 'last_name'
                       )}
         ),
    )

    search_fields = ('email',)
    ordering = ('id',)


admin.site.register(User, CustomUserAdmin)
