from django.contrib import admin

# Register your models here.

# Register your models here.

from .models import *

# Register your models here.

# admin.site.register(query_form),
# admin.site.register(slider),

@admin.register(q_form)
class ContactCommentModelAdmin(admin.ModelAdmin):
    search_fields = [
        'id',
        'name',
        'email',

    ]
    list_display = ['name','id','email','phone']

# admin.site.register(q_form),
admin.site.register(email_data),
admin.site.register(blog),

@admin.register(Course)
class CourseCommentModelAdmin(admin.ModelAdmin):
    search_fields = [
        'id',
        'course_title',
    ]
    list_display = ['course_title','id','course_price','course_img']

@admin.register(StuReview)
class StuReviewModelAdmin(admin.ModelAdmin):
    search_fields = [
        'id',
        'stu_name',
    ]
    list_display = ['stu_name','id','stu_descp']

@admin.register(Event)
class EventCommentModelAdmin(admin.ModelAdmin):
    search_fields = [
        'id',
        'event_title',
    ]
    list_display = ['event_title','id','event_location','event_date','event_img']