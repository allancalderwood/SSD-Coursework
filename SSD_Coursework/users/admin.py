from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Role

# Register your models here.

#  inline admin descriptor for role
class RoleInLine(admin.StackedInline):
    model = Role
    can_delete = False
    verbose_name_plural = 'role'

# new user admin
class UserAdmin(BaseUserAdmin):
    inlines = (RoleInLine,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
