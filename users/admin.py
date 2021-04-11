from django.contrib import admin
from .models import Users

class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "username", "email", "role")
    search_fields = ("username",)


admin.site.register(Users, UserAdmin)