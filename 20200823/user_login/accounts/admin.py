#accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'phone', 'email', 'address']
    fieldsets = (*UserAdmin.fieldsets, 
                    ('Thông tin khác', {
                        'fields': ['phone', 'address']
                    })
                )

admin.site.register(CustomUser, CustomUserAdmin)
