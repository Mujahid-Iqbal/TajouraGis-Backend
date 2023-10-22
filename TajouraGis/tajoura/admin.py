from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # List the fields you want to display in the admin list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    # Exclude the password field from the admin change form
    exclude = ('password',)

# Register your custom user model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)

