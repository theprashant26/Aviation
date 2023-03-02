from django.shortcuts import redirect, render,HttpResponseRedirect
from django.urls import reverse
from Student.forms import Student_detailForm
from Home.models import *
import sweetify
from django.views import View
from django.shortcuts import HttpResponse
from django.contrib import messages
# Create your views here.


def Home(request):
    course = Course.objects.all().order_by('id').reverse()[0:3]
    stur = StuReview.objects.all().order_by('id').reverse()
    eve = Event.objects.all().order_by('id').reverse()
    return render(request, 'Home/index.html',{'course':course,'stur':stur,'eve':eve})


def email_Data(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        emaildata = email_data.objects.create(email=email)
        emaildata.save()
        messages.info(request,"Successfully Submitted")
        # sweetify.success(request, 'Hey', text= 'You have successfully Subscribed', persistent='Done')
        return redirect('Home:Home')
        

def Addstudent(request):
    form = Student_detailForm()
    context = {
        'form':form
    }
    return render(request, 'Home/Addstudent.html' , context)
def About(request):
    return render(request, 'Home/about.html')

def ContactUs(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        qform = q_form.objects.create(name = name , email=email , phone = phone , message = message,subject=subject)
        qform.save()
        messages.info(request,"Successfully Submitted")
        # sweetify.success(request, 'Hey', text= 'You have successfully filled the form', persistent='Done')
        return HttpResponseRedirect(reverse('Home:ContactUs'))
    return render(request, 'Home/contactUs.html')

class blogpage(View):
    def get(self,request):
        bl = blog.objects.all()
        return render(request, 'Home/blog.html', {'bl':bl })

class blogdetailview(View):
    def get(self,request,slug):
        Blog = blog.objects.get(blog_slug=slug)
        Blog_object=blog.objects.get(blog_slug=slug)
        Blog_object.save()

        return render(request, 'Home/blogdetail.html',{'Blog':Blog})

class eventdetailview(View):
    def get(self,request,slug):
        event = Event.objects.get(event_slug=slug)
        event_object=Event.objects.get(event_slug=slug)
        event_object.save()

        return render(request, 'Home/eventdetail.html',{'event':event})

def TAC(request):
    return render(request, 'Home/titan.html')
def TAC2(request):
    return render(request, 'Home/TAC.html')

class allcourse(View):
    def get(self,request):
        course = Course.objects.all().order_by('id').reverse()[0:6]
        return render(request, 'Home/allcourse.html', {'course':course})

class coursedetailview(View):
    def get(self,request,slug):
        course = Course.objects.get(course_slug=slug)
        course_object=Course.objects.get(course_slug=slug)
        course_object.save()

        return render(request, 'Home/coursedetail.html',{'course':course})

def privacypol(request):
    return render(request, 'Home/privacypolicy.html')




