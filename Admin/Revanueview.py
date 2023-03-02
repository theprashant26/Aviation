
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.shortcuts import render,redirect

from Student.models import Order, Student_detail
# from .models import Student_detail #,Course, courses_det ,slider,query_form

# from django.http import HttpResponse, HttpResponseRedirect

# from django.core.mail import send_mail
# from Admission.settings import EMAIL_HOST_USER
import string
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import user_passes_test
import datetime
from datetime import *

from django.urls import reverse
# from .forms import  CourseForm, Student_detailForm,Student_detail_editForm , newuserform
from django.forms.models import model_to_dict
import random
# import razorpay 
import math

from datetime import datetime, timedelta 
import datetime
from django.shortcuts import render
# @login_required
def Revenue(request):
    # pay =  Student_detail.objects.filter(Payment=True)
    rev = Order.objects.all()
    Totalrevenue = sum(rev.values_list('amount' ,flat=True))
    data =round( Totalrevenue,2 )
    # today revenue
    # paydate = rev.date
    # print(paydate)
    Date = datetime.datetime.now().date()
    dayrev = Order.objects.filter(date = Date )
    print(dayrev)        
    Dayrevenue = round(sum(dayrev.values_list('amount' ,flat=True)), 2)

    day = Date 

    
    day_1 = (Date + timedelta(days = -1))
    dayrev1 = Order.objects.filter(date = day_1 )
    Day1revenue = sum(dayrev1.values_list('amount' ,flat=True))
    day_2 = (Date + timedelta(days = -2))
    dayrev2 = Order.objects.filter(date = day_2 )
    Day2revenue = sum(dayrev2.values_list('amount' ,flat=True))
    day_3 = (Date + timedelta(days = -3))
    dayrev3 = Order.objects.filter(date = day_3 )
    Day3revenue = sum(dayrev3.values_list('amount' ,flat=True))
    day_4 = (Date + timedelta(days = -4))
    dayrev4 = Order.objects.filter(date = day_4 )
    Day4revenue = sum(dayrev4.values_list('amount' ,flat=True))
    day_5 = (Date + timedelta(days = -5))
    dayrev5 = Order.objects.filter(date = day_5 )
    Day5revenue = sum(dayrev5.values_list('amount' ,flat=True))
    

    # today revenue
    # months revenue
    Date = datetime.datetime.now().date()

    # print(Date)

    month_0 = Date 
    year_0 = month_0.year
    month_0 = month_0.month
    # print(month_1 , year_1 , 'i am month')
    monthrev0 = Order.objects.filter(date__year = year_0 ,date__month = month_0 )
    month0revenue = round( sum(monthrev0.values_list('amount' ,flat=True)) , 2)
    print(month0revenue , 'i am month revenu' ,month_0)
    month_1 = (Date + timedelta( -31))
    year_1 = month_1.year
    month_1 = month_1.month
    # print(month_1 , year_1 , 'i am month')
    monthrev1 = Order.objects.filter(date__year = year_1 ,date__month = month_1 )
    month1revenue = sum(monthrev1.values_list('amount' ,flat=True))

    month_2 = (Date + timedelta( -62))
    year_2 = month_2.year
    month_2 = month_2.month
    monthrev2 = Order.objects.filter(date__year = year_2 ,date__month = month_2)
    month2revenue = sum(monthrev2.values_list('amount' ,flat=True))

    month_3 = (Date + timedelta( -93))
    year_3 = month_3.year
    month_3 = month_3.month
    monthrev3 = Order.objects.filter(date__year = year_3 ,date__month = month_3)
    month3revenue = sum(monthrev3.values_list('amount' ,flat=True))

    month_4 = (Date + timedelta( -124))
    year_4 = month_4.year
    month_4 = month_4.month
    monthrev4 = Order.objects.filter(date__year = year_4 ,date__month = month_4)
    month4revenue = sum(monthrev4.values_list('amount' ,flat=True))

    month_5 = (Date + timedelta( -155))
    year_5 = month_5.year
    month_5 = month_5.month
    monthrev5 = Order.objects.filter(date__year = year_5 ,date__month = month_5)
    month5revenue = sum(monthrev5.values_list('amount' ,flat=True))

    month_6 = (Date + timedelta( -186))
    year_6 = month_6.year
    month_6 = month_6.month
    monthrev6 = Order.objects.filter(date__year = year_6 ,date__month = month_6)
    month6revenue = sum(monthrev6.values_list('amount' ,flat=True))
    month_7 = (Date + timedelta( -217))
    year_7 = month_7.year
    month_7 = month_7.month
    monthrev7 = Order.objects.filter(date__year = year_7 ,date__month = month_7)
    month7revenue = sum(monthrev7.values_list('amount' ,flat=True))
    month_8 = (Date + timedelta( -248))
    year_8 = month_8.year
    month_8 = month_8.month
    monthrev8 = Order.objects.filter(date__year = year_8 ,date__month = month_8)
    month8revenue = sum(monthrev8.values_list('amount' ,flat=True))
    month_9 = (Date + timedelta( -279))
    year_9 = month_9.year
    month_9 = month_9.month
    monthrev9 = Order.objects.filter(date__year = year_9 ,date__month = month_9)
    month9revenue = sum(monthrev9.values_list('amount' ,flat=True))
    month_10 = (Date + timedelta(-310))
    year_10 = month_10.year
    month_10 = month_10.month
    monthrev10 = Order.objects.filter(date__year = year_10 ,date__month = month_10)
    month10revenue = sum(monthrev10.values_list('amount' ,flat=True))
    month_11 = (Date + timedelta(-341))
    year_11 = month_11.year
    month_11 = month_11.month
    monthrev11 = Order.objects.filter(date__year = year_11 ,date__month = month_11)
    month11revenue = sum(monthrev11.values_list('amount' ,flat=True))
    # month_12 = (Date + timedelta(-371))
    # year_12 = month_12.year
    # month_12 = month_12.month
    # monthrev12 = Order.objects.filter(date__year = year_12 ,date__month = month_12)
     
    import calendar
    month_0 = calendar.month_name[month_0] 
    month_1 = calendar.month_name[month_1] 
    month_2 = calendar.month_name[month_2] 
    month_4 = calendar.month_name[month_4] 
    month_5 = calendar.month_name[month_5] 
    month_7 = calendar.month_name[month_6] 
    month_8 = calendar.month_name[month_8] 
    month_9 = calendar.month_name[month_9] 
    month_10 = calendar.month_name[month_10] 
    month_11 = calendar.month_name[month_11] 
    # month_12 = calendar.month_name[month_12] 
    # print(month_12)
    # month12revenue = sum(monthrev12.values_list('amount' ,flat=True))
    # dayr = Order.objects.filter(date__year = 2022 , date__month = 2 )

    # print(dayr  , "test")
    monthrev = [
        month_0,
        month_1,
        month_2,
        month_3,
        month_4,
        month_5,
        month_6,
        month_7,
        month_8,
        month_9,
        month_10,
        month_11,
        # month_12,   
        ]
    monthrevenue = [
        month0revenue,
        month1revenue,
        month2revenue,
        month3revenue,
        month4revenue,
        month5revenue,
        month6revenue,
        month7revenue,
        month8revenue,
        month9revenue,
        month10revenue,
        month11revenue,


    ]   
    # months revenue
    # user count
    # users_no = Student_detail.objects.all().count()
    # users_no_paid = Student_detail.objects.filter(Payment=True).count()

    # user count
    
    context = { 'data':data , 'Dayrevenue':Dayrevenue ,
            #    'users_no' : users_no ,'users_no_paid':users_no_paid , 
               'day':day,
    'day_1':day_1,
    'day_2':day_2,
    'day_3':day_3,
    'day_4':day_4,
    'day_5':day_5,
    'Day1revenue':Day1revenue,
    'Day2revenue':Day2revenue,
    'Day3revenue':Day3revenue,
    'Day4revenue':Day4revenue,
    'Day5revenue':Day5revenue,
    # monthrev 
    'monthrev':monthrev,
    'monthrevenue':monthrevenue,
    # 'month_12':month_12
    # monthrev
    # rev list
    'rev':rev,
    # rev list
     }


    return render(request,'Admin/Revanue.html', context)
def paymentlist(request):
    rev = Order.objects.all()
    user = request.user
    context = {
        'rev':rev
    }
    if user.is_superuser:
        
        return render(request,'Admin/paymentlist.html', context)
    elif user.is_staff:
        return render(request,'Teacher/paymentlist.html', context)
        
def duelist(request):
    due = Student_detail.objects.all()
    # data1 = due
    
    user = request.user
    context = {
        'due':due,
        
    }
    if user.is_superuser:
        return render(request,'Admin/duelist.html', context)
    elif user.is_staff:
        return render(request,'Teacher/duelist.html', context)
        