from django.contrib import admin
from .models import Profile

class UserProfileAdmin(admin.ModelAdmin):
    fields = ('image_tag', 'image',)
    readonly_fields = ('image_tag',)

admin.site.register(Profile, UserProfileAdmin)
