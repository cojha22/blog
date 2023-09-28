from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.forms import UserChangeForm, UserCreationForm
from accounts.models import User

# Register your models here.


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = [
        "email",
        "username",
        "is_admin",
        "is_active",
        "is_superuser",
    ]

    list_filter = (
        "is_admin",
        "is_active",
        "is_superuser",
    )

    fieldsets = ((None, {"fields": ("email",)}),
                 ("personal Information", {"fields": ("username",)}),
                 ("Permissions", {"fields": [
                  "is_admin", "is_active", "is_superuser",]}),
                 )

    add_fieldsets = (None, {"class": ("wide",),
                            "fields":
                            ("email",
                             "username",
                             "password",
                             "password2",
                             ),
                            },
                     )

    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, UserAdmin)
