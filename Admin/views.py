import email
from email.message import EmailMessage
from multiprocessing import context
import random
import string
from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from Admin.Leacturemodels import Lecture
from Admin.Lectureforms import LectureForm
from Admin.forms import CourseForm, UserProfileform
from Admin.models import Course, UserProfile, newuserform
import sweetify
from django.core.mail import send_mail

from django.contrib.auth.decorators import user_passes_test
from BRD.settings import EMAIL_HOST_USER , EMAIL_HOST_USER1

from Student.forms import Student_detailForm
from Student.models import Student_detail
from django.contrib.auth import authenticate, login
# Create your views here.
EMAIL_HOST_USER = EMAIL_HOST_USER1

def Home(request):
    user = request.user
    if user.is_superuser:
        
        return render(request, 'Admin/Home.html')
    elif user.is_staff:
        return render(request, 'Teacher/Home.html')
    elif user.is_authenticated :   
        return render(request, 'Students/Home.html')
    else:
        print('i am run')
        return redirect('accounts:login')
@user_passes_test(lambda u: u.is_superuser)
def Addteacher(request):
    # sweetify.success(request, 'Hey ', text='Good job! Successfully Applied', persistent='Done')
    form = newuserform()
    if request.method == 'POST':
        form = newuserform(request.POST)    
        if form.is_valid():
            form.save()
            sweetify.success(request, 'You did it', text='Teacher added', persistent='Done')
            # email = form.cleaned_data.get('username')
        # Check to see if any users already exist with this email as a username.  
    context = {
        'form':form
    }
    return render(request , 'Admin/Addteacher.html' , context)
def Addteacherdetail(request):
    user = request.user
    if UserProfile.objects.filter(user = user).exists():
        data = UserProfile.objects.get(user = user)
        form = UserProfileform(request.POST,instance=data)
        if request.method == "POST":
            # UserProfile.objects.get(user = user)
            if form.is_valid():
                print('i am running')
                form.save()                
                sweetify.success(request, 'Hey', text='Details Updated', persistent='Done')   
                return redirect('Admin:AdminProfile')           
            else:
                sweetify.warning(request, 'Hey', text='Somthing went wrong! inuser profile', persistent='Done')
                    
                  
                return redirect('Admin:AdminProfile')
    else:
        data= UserProfile.objects.create(user=user)                     
        data.save()
        return redirect('Admin:AdminProfile') 
            
            
        # phone = request.POST.get('phone')
        # gender = request.POST.get('gender')
        # about = request.POST.get('about')
            # UserProfiled = UserProfile.objects.get(user = user)
               
                
# @user_passes_test(lambda u: u.is_superuser)
def Profile(request):
    user = request.user
    print(user)
    if UserProfile.objects.filter(user = user).exists():
        data = UserProfile.objects.get(user = user)
        form = UserProfileform(instance=data )  
        if user.is_superuser:
            context = {
            'data': data, 
            'form':form,
            }
            return render(request, 'Admin/Profile.html' , context)
        elif user.is_staff:
            context = {
            'data': data, 
            'form':form,}
            
            return render(request, 'Teacher/Profile.html' , context)    
        else:
            data2 = Student_detail.objects.get(Email = user)
            
            context = {
            'data2': data2, 
            'data': data, 
            'form':form,
        }
        return render(request, 'Students/Profile.html' , context)
    else:
        data1= UserProfile.objects.create(user=user)                     
        data1.save()
        return redirect('Admin:AdminProfile')
    
def Base2(request):
    sweetify.success(request, 'Hey ', text='Good job! Successfully Applied', persistent='Done')

    return render(request , 'Base/adminbase.html')    
@user_passes_test(lambda u: u.is_superuser)
def Courseboard(request):
    form = CourseForm()
    course = Course.objects.all()
    # print(form)
    context = {
        'form': form,
        'Course':course,
    }
    
    return render(request , 'Admin/Courseboard.html' , context )

def Addcourse(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            Course_name =  form.cleaned_data['Course_name']
        
            if Course.objects.filter(Course_name=Course_name ).exists():
                user = request.user
                if user.is_superuser:
                    return redirect('Admin:Courseboard')
                else:
                    return redirect('Teacher:TCourseboard')    
            else:    
                form.save()
                user = request.user
                if user.is_superuser:
                    return redirect('Admin:Courseboard')
                else:
                    return redirect('Teacher:TCourseboard')
                
def Course_edit(request , id ):
    item = Course.objects.get(id = id)
    form = CourseForm(request.POST  ,instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            user = request.user
            if user.is_superuser:
                return redirect('Admin:Courseboard')
            else:
                return redirect('Teacher:TCourseboard')        
    else:
        form = CourseForm(instance=item)      
    context = {
        'form' : form
    }

    return render(request , 'Admin/Course_edit.html' , context  )                
        
def Course_delete(request , id ):
    item = Course.objects.get(id = id)
    item.delete()
    user = request.user
    if user.is_superuser:
        return redirect('Admin:Courseboard')
    else:
        return redirect('Teacher:TCourseboard')
#Add student

def Studentboard(request):
    form = Student_detailForm()
    Student = Student_detail.objects.all()
    context = {
        'form':form,
        'Student':Student
    }
    user = request.user
    if user.is_superuser:
        return render(request , 'Admin/Studentboard.html' ,context )
    elif user.is_staff:
        return render(request , 'Teacher/Studentboard.html' ,context )
    
def Student_delete(request , id):
    
    Student = Student_detail.objects.get(id = id )
    Email = Student.Email
    user = User.objects.get(email = Email)
    if UserProfile.objects.filter(user = user).exists():
        UserProfile.objects.get(user = user).delete()
    Student.delete()
    user.delete()
    user = request.user
    if user.is_superuser:
        return redirect('Admin:Studentboard')
    else:
        return redirect('Admin:Studentboard')
def Student_edit(request , id):
    user = request.user
    
    Student = Student_detail.objects.get(id = id )
    form = Student_detailForm(instance=Student)
    context = {
        'form':form , 
        'id':id
    }
    
    if request.method == "POST":
        form = Student_detailForm(request.POST , request.FILES ,instance=Student)
        if form.is_valid():
            
            form.save()
            if user.is_superuser:
                return redirect('Admin:Studentboard')
            elif user.is_staff:
                return redirect('Admin:Studentboard')
             
    
    if user.is_superuser:
        return render(request, 'Admin/Student_edit.html' , context)
    elif user.is_staff:
        return render(request,'Teacher/Student_edit.html', context)
    


def Addstudent(request):
    form = Student_detailForm()
    context = {
        'form':form
    }
    return render(request , 'Admin/Addstudent.html' , context )
    
def ADDstudent(request):
    # form = Student_detailForm()
    user = request.user
    # context = {
    #     'form':form
    # }
    if request.method == 'POST':
        print('i am post')
        form = Student_detailForm( request.POST , request.FILES )
        
        
        if form.is_valid():
            print('i am valid')
            UEmail =  form.cleaned_data['Email']
            print(UEmail)
            Fname =  form.cleaned_data['Name']
            if Student_detail.objects.filter(Email = UEmail).exists() or User.objects.filter(email = UEmail).exists():
                sweetify.warning(request, 'Hey ', text= f'{UEmail} Email Aready takken', persistent='Done')
                if user.is_superuser:
                    return redirect('Admin:Studentboard')
                elif user.is_staff:
                    return redirect('Admin:Studentboard')
                else: 
                    return redirect('Home:Base')
            else:
                
                # user create
                email = UEmail
                # email = EmailMessage('title', 'body', to=[email])
                # email.send()
                # generating random strings 
                N = 7
                res = ''.join(random.choices(string.ascii_uppercase +
                        string.digits, k = N))
                print("The generated random string : " + str(res))
                message = "your id and password is : " + " Email:- " + email + " Password:- " + res + " , " + " " + "Your account will be activated after first payment "
                subject = ' Student Admission'
                print('i am runing')
                # user create 
                user = User.objects.create_user(email,password=res ,email = UEmail, first_name = Fname )
                try:
                    send_mail(subject, 
                        message, EMAIL_HOST_USER, [email], fail_silently = False)
                    send_mail(subject, 
                        message, EMAIL_HOST_USER, [EMAIL_HOST_USER], fail_silently = False)
                except:
                    pass    
                # user create
                form.save()
                sweetify.success(request, f'Hey {Fname}', text= f'Account created your password sent to mail {UEmail} and your account will be activated after first payment ' , persistent='Done')
                user = request.user
                if user.is_superuser:
                    return redirect('Admin:Studentboard')
                elif user.is_staff:
                    return redirect('Admin:Studentboard')
                else:
                    new_user = authenticate(username=UEmail,
                                    password=res,
                                    )
                    login(request, new_user)
                    
                    return redirect('Student:payment')
        else:
            sweetify.success(request, 'Hey', text= 'Form is not valid', persistent='Done')
            return redirect('Home:Base')
            
            
    # return render(request , 'Admin/Addstudent.html' , context )
                
#Add student  
def handler404(request,*args,**argv):
    return render(request,'Base/error.html')

