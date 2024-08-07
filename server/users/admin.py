from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

class UserAdminConfig(UserAdmin):

    search_fields = ('email', 'user_name', 'first_name',)
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields':('email', 'user_name')}),
        ('Permissions', {'fields': ('is_active','is_staff')}),
    )

    add_fieldsets =(
        (None,{
            'classes': ('wide',),
            'fields':('email', 'user_name', 'password1', 'password2', 'is_active', 'is_staff')}
            ),
    )


admin.site.register(NewUser, UserAdminConfig)

