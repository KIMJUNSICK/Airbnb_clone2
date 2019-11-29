from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# admin.ModelAdmin -> UserAdmin
# Import & Use: this is the essential reason for developing project with Django
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom  User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthday",
                    "language",
                    "currency",
                    "superhost",
                ),
            },
        ),
    )
