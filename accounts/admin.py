from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'join_date']
    list_filter = ['city', 'join_date']
    search_fields = ['user__first_name', 'city', 'bio']
    list_editable = ['city']


admin.site.register(Profile, ProfileAdmin)
