from django.contrib import admin

# Register your models here.

# from .models import Course  
from .models import  Student_detail ,Order,Student_Payment

# Register your models here.
class StudentDdetailAdmin(admin.ModelAdmin):
    list_display = ('Name', 'id', 'Email', 'Aadhaar', 'Admission_no', 'Course_name', 'date_of_joining', 'paid_amount', 'State', 'City', 'District')
    search_fields = [
        'Name',
        'Email',
        'Aadhaar',
        'Admission_no',
    ]
    list_pr_page = 25

class StudentPaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'email', 'Admission_no', 'payment_id', 'Amount')
    search_fields = [
        'name',
        'user',
        'email',
    ]

admin.site.register(Student_detail, StudentDdetailAdmin)
admin.site.register(Order)
admin.site.register(Student_Payment, StudentPaymentAdmin)

