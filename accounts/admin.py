from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Profile


class ProfileInline(admin.StackedInline):
    model         = Profile
    can_delete    = False
    verbose_name  = 'Profile'
    fk_name       = 'user'


class CustomUserAdmin(UserAdmin):
    inlines          = [ProfileInline]
    list_display     = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined']
    list_filter      = ['is_staff', 'is_active', 'date_joined']
    search_fields    = ['username', 'email', 'first_name', 'last_name']
    ordering         = ['-date_joined']


# Unregister default User and register our custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display  = ['user', 'phone', 'city', 'state', 'pincode']
    search_fields = ['user__username', 'user__email', 'phone', 'city']
    list_filter   = ['state', 'city']