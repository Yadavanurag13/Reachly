from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "created_at",
    )
    list_filter = (
        "is_active",
        "is_staff",
        "is_superuser",
    )
    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
    )
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": (
            "first_name",
            "last_name",
            "email",
            "mobile_number",
            "avatar",
        )}),
        (_("Status"), {"fields": (
            "is_active",
            "is_staff",
            "is_superuser",
        )}),
        (_("Important dates"), {"fields": (
            "created_at",
            "updated_at",
        )}),
        (_("Groups and Permissions"), {
            "fields": (
                "groups",
                "user_permissions",
            ),
        }),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username",
                "email",
                "password1",
                "password2",
                "is_staff",
                "is_superuser",
            ),
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ("username", "email")
        return self.readonly_fields
    
    def save_model(self, request, obj, form, change):
        if not change:  # Creating a new user
            obj.is_active = True
        super().save_model(request, obj, form, change) 