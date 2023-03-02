from django.contrib import admin

# Register your models here.

from .models import Course  ,UserProfile
from .Leacturemodels import Lecture  

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'phone',
    )
    search_fields = [
        'id',
    ]

admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(UserProfile, UserProfileAdmin)