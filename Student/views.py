
from datetime import datetime, timedelta
from email import message
from multiprocessing import context
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from razorpay import Payment
import razorpay
from django.views.decorators.csrf import csrf_exempt
import razorpay
from Admin.Leacturemodels import Lecture
from calendar import week

import datetime 
from datetime import *

from Admin.models import Course, UserProfile
from django.contrib.auth.decorators import login_required
from BRD import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
# from django.template import Context, loader
from BRD.settings import EMAIL_HOST_USER , EMAIL_HOST_USER1
# this is for new mail
from django.template import Context
# from django.template.loader import render_to_string, get_template
# from django.core.mail import EmailMessage
# this is for new mail
from Student.models import Order, Student_detail
import sweetify
EMAIL_HOST_USER = EMAIL_HOST_USER1

# Create your views here.
@login_required
def Profile(request):
    user = request.user
    User = request.user.username
    test = Student_detail.objects.get(Email=User).id
    test2 = Student_detail.objects.get(pk=test) 
    course = test2.Course_name.id
    course = Course.objects.get(id = course)
    course = course.Price
    amount = round( (course/3)*100 , 0)
    if UserProfile.objects.filter(user = user).exists():
        data = UserProfile.objects.get(user = user)
        print(data)
        context = {
            'data': data,
            'amount':amount
        }
        return render(request, 'Students/Profile.html' , context)
    else:    
        return render(request, 'Students/Profile.html' )

def Lecturevideo(request):
    User = request.user.username
    test = Student_detail.objects.get(Email=User).id
    test2 = Student_detail.objects.get(pk=test) 
    d = test2.date_of_joining
    now = date.today()
    User = request.user.username
    test = Student_detail.objects.get(Email=User).id
    test2 = Student_detail.objects.get(pk=test) 
    # course logic Price
    course = test2.Course_name.id
    lecture = Lecture.objects.filter(course = course)
    
    course = Course.objects.get(id = course)
    course = course.Price
    paid_price = test2.paid_amount
    d = test2.date_of_joining
    now = date.today()

    # print(course)
    # course logic
    # date logic for false payment
    d = test2.date_of_joining
    first = (d + timedelta(days = 30))
    second = (d + timedelta(days = 60))
    third = (d + timedelta(days = 90))
    now = date.today()
    print(first)
    if now <= first and int((course/3)) <= paid_price  and now <= second :     
        test2.Payment = True
        test2.save()
        print('first')
    elif now <= second and int((course/2)) <= paid_price and now <= third :
        test2.Payment = True
        test2.save()
        print('2nd')
    elif now <= third and int((course)) <= paid_price :
        test2.Payment = True
        test2.save()
        print('3rd')
    else:
        print('else')
        test2.Payment = False
        test2.save()
        
    # course logic Price
    
    print(lecture)
        # date logic for video slicing
    week1 = (d + timedelta(days = 0))
    week2 = (d + timedelta(days = 7))
    week3 = (d + timedelta(days = 14))
    week4 = (d + timedelta(days = 21))
    week5 = (d + timedelta(days = 28))
    week6 = (d + timedelta(days = 35))
    week7 = (d + timedelta(days = 42))
    week8 = (d + timedelta(days = 49))
    week9 = (d + timedelta(days = 56))
    week10 = (d + timedelta(days = 63))
    week11 = (d + timedelta(days = 70))
    week12 = (d + timedelta(days = 77))
    course = test2.Course_name.id
    course = Course.objects.get(id = course)
    course = course.Price
    amount = round( (course/3)*100 , 0)
    if  week1 <= now and now <= week2 and now <= week3 and now <= week4 and now <= week5 and now <= week6 and now <= week7 and now <= week8 and now <= week9 and now <= week10 and now <= week11 and now <= week12:
        lecture1 = lecture[0:4]
        print('i am 1')
        context = {
        'lecture': lecture1,
        'Test':test2 ,
        'amount':amount,

        }
        return render(request,'Students/Lecturevideo.html',context)


    elif now >= week2 and now <= week3 and now <= week4 and now <= week5 and now <= week6 and now <= week7 and now <= week8 and now <= week9 and now <= week10 and now <= week11 and now <= week12:  
        lecture1 = lecture[0:10]
        print('i am 2')

        context = {
        'lecture': lecture1,
        'Test':test2,
        'amount':amount,
        

        }
        return render(request,'Students/Lecturevideo.html',context)
    elif now >= week3 and now <= week4 and now <= week5 and now <= week6 and now <= week7 and now <= week8 and now <= week9 and now <= week10 and now <= week11 and now <= week12:  
        lecture1 = lecture[0:18]
        print('i am 2')

        context = {
        'lecture': lecture1,
        'Test':test2,
        'amount':amount,
        

        }
        return render(request,'Students/Lecturevideo.html',context)
    elif now >= week4  and now <= week5 and now <= week6 and now <= week7 and now <= week8 and now <= week9 and now <= week10 and now <= week11 and now <= week12:  
        lecture1 = lecture[0:25]
        print('i am 2')

        context = {
        'lecture': lecture1,
        'Test':test2,
        'amount':amount,
        

        }
        return render(request,'Students/Lecturevideo.html',context)
    elif now >= week5   and now <= week6 and now <= week7 and now <= week8 and now <= week9 and now <= week10 and now <= week11 and now <= week12:  
        lecture1 = lecture[0:32]
        print('i am 2')

        context = {
        'lecture': lecture1,
        'Test':test2,
        'amount':amount,
        

        }
        return render(request,'Students/Lecturevideo.html',context)
    elif now >= week6 and now <= week7 and now <= week8 and now <= week9 and now <= week10 and now <= week11 and now <= week12:  
        lecture1 = lecture[0:40]
        print('i am 2')

        context = {
        'lecture': lecture1,
        'Test':test2,
        'amount':amount,
        

        }
        return render(request,'Students/Lecturevideo.html',context)
    elif now >= week7 and now <= week8 and now <= week9 and now <= week10 and now <= week11 and now <= week12:  
        lecture1 = lecture[0:45]
        print('i am 2')

        context = {
        'lecture': lecture1,
        'Test':test2,
        'amount':amount,
        

        }
        return render(request,'Students/Lecturevideo.html',context)
    elif now >= week8  and now <= week9 and now <= week10 and now <= week11 and now <= week12:  
        lecture1 = lecture[0:47]
        print('i am 2')

        context = {
        'lecture': lecture1,
        'Test':test2,
        'amount':amount,
        

        }
        return render(request,'Students/Lecturevideo.html',context)
    elif now >= week9 and now <= week10 and now <= week11 and now <= week12:  
        lecture1 = lecture[0:50]
        print('i am 2')

        context = {
        'lecture': lecture1,
        'Test':test2,
        'amount':amount,
        

        }
        return render(request,'Students/Lecturevideo.html',context)
    elif now >= week10  and now <= week11 and now <= week12:  
        lecture1 = lecture[0:55]
        print('i am 2')

        context = {
        'lecture': lecture1,
        'Test':test2,
        'amount':amount,
        

        }
        return render(request,'Students/Lecturevideo.html',context)
    elif now >= week11  and now <= week12:  
        lecture1 = lecture[0:58]
        print('i am 2')

        context = {
        'lecture': lecture1,
        'Test':test2,
        'amount':amount,
        

        }
        return render(request,'Students/Lecturevideo.html',context)

    else :
        print('i am 3')

        lecture1 = lecture
        context = {
            
            'lecture': lecture1,
            'Test':test2,
            'amount':amount,
            
        }
        return render(request,'Students/Lecturevideo.html',context)
    

@login_required
def payment(request):
    User = request.user.username
    test = Student_detail.objects.get(Email=User).id
    test2 = Student_detail.objects.get(pk=test) 
    course = test2.Course_name.id
    course = Course.objects.get(id = course)
    course = course.Price
    amount = round( (course/3)*100 , 0)
    # print(amount)
    #if request.method == "POST":
        # name = request.POST.get('name')
        # amount = course/3
        # print('i am runing')
    client = razorpay.Client(
    auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET_KEY))
    payment = client.order.create({'amount': amount, 'currency': 'INR'  ,
    'payment_capture': '0'})
    razorpay_order_ID = payment['id']
    
    
    callback_url = 'paymenthandler/'
        # signature_id = payment['id'][2]
        # print(signature_id)
        # order_id = payment[]
        # print(order_id)
    
        
    
    if test2.paid_amount <= test2.Course_name.Price:
        Due =  test2.Course_name.Price - round(test2.paid_amount , 0)
    else:
        Due = 0    
    context =  {
        'item':test2,
        'Due':Due,
        
    }
    context['razorpay_order_id'] = razorpay_order_ID
    context['razorpay_merchant_key'] = settings.RAZORPAY_API_KEY
    context['razorpay_amount'] = amount
    context['currency'] = 'INR'
    context['callback_url'] = callback_url
    return render(request, 'Students/payment.html', context)
    
    
client = razorpay.Client(
        auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET_KEY)) 
from django.views.decorators.csrf import csrf_exempt   
@csrf_exempt
def paymenthandler(request):
    User = request.user.username
    test = Student_detail.objects.get(Email=User).id
    test2 = Student_detail.objects.get(pk=test) 
    
    course = test2.Course_name.id
    course = Course.objects.get(id = course)
    course = course.Price
    amount = round( (course/3)*100 , 0)
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            user = request.user
            order = Order.objects.create(
            name=user.username,  amount=amount/100 , payment_id = payment_id , provider_order_id = razorpay_order_id , user = user ,status = 'done'
        )
            order.save()
            test2.Payment = True 
            # print(Date)
            # Date = Date.date2
            pri_amount = test2.paid_amount
            test2.paid_amount = ((amount/100) + pri_amount)
            test2.save()
            # print(payment_id)
            # print('i am line 345')
            subject = 'INVOICE'
            # message = 'i am working'
            message = 'Payment Done'
            email = test2.Email
            now = datetime.now()
            
            Context = {'context': test2, 'data':payment_id , 'datenow':now }
            send_mail(subject, 
                    message, EMAIL_HOST_USER, [EMAIL_HOST_USER], fail_silently = False)
            html_message = render_to_string('Students/invoicemail.html', Context )
            plain_message = strip_tags(html_message)
            # print('i am line 349')
            send_mail(subject, 
                    plain_message, EMAIL_HOST_USER, [EMAIL_HOST_USER],html_message=html_message, fail_silently = False)
            # print('i am mail')
            send_mail(subject, 
                    plain_message, EMAIL_HOST_USER , [email],html_message=html_message, fail_silently = False)
            # print('i am mail2')
            
            # verify the payment signature.
            util = razorpay.Utility(client)
            util =  util.verify_payment_signature(params_dict)
            sweetify.success(request, 'Hey', text= 'Your invoice sent to your mail', persistent='Done')
            
            return render(request,'Students/invoice.html', {'context': test2, 'data':payment_id , 'datenow':now } )
            # return redirect('Student:Lecturevideo')  
        except:
            # if we don't find the required parameters in POST data
            now = datetime.now()
            sweetify.success(request, 'Hey', text= 'Your invoice in Payment status ', persistent='Done')
            return render(request,'Students/invoice.html', {'context': test2, 'data':payment_id ,'datenow':now   } )
            # return redirect('Student:payment')
    else:
       # if other than POST request is made.
        # return HttpResponseBadRequest() 
        sweetify.warning(request, 'Hey', text= 'Something went wrong!!! ', persistent='Done')
        return redirect('Student:payment')   
    
    
    
def paymentstatus(request):
    # data = Order.objects.filter(user = request.user).id
    data = Order.objects.filter(user = request.user)
    
    
    context = {
        'data':data,
        
        
    }
    return render(request, 'Students/paymentstatus.html' ,context)    

def invoice2(request , id):
    data = Order.objects.get(id = id)
    User = request.user.username
    test = Student_detail.objects.get(Email=User).id
    test2 = Student_detail.objects.get(pk=test) 
    
    context = {
        'context': test2,
        'data':data,
    }
    return render(request, 'Students/invoice2.html' ,context)    
    