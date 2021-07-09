from django.contrib import admin
from .models import UserProfile, User

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'participating')
    search_fields = ('user', )

admin.site.register(UserProfile, UserProfileAdmin)