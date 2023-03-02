import email
from multiprocessing import context
from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from Admin.Leacturemodels import Lecture
from Admin.Lectureforms import LectureForm
from Admin.forms import CourseForm
from Admin.models import Course, UserProfile, newuserform
import sweetify

# Create your views here.
from django.contrib.auth.decorators import user_passes_test

from Student.forms import Student_detailForm

@user_passes_test(lambda u:u.is_staff, login_url=reverse_lazy('foo'))
def Profile(request):
    user = request.user
    if UserProfile.objects.filter(user = user).exists():
        data = UserProfile.objects.get(user = user)
        print(data)
        context = {
            'data': data
        }
    else:
        pass    
    return render(request, 'Teacher/Profile.html' , context)

@user_passes_test(lambda u:u.is_staff, login_url=reverse_lazy('foo'))
def Lectureboard(request):
    form = LectureForm()
    Lecture1 = Lecture.objects.all()
    # print(form)
    context = {
        'form': form,
        'Lecture':Lecture1,
    }
    return render(request , 'Teacher/Lectureboard.html' , context )
@user_passes_test(lambda u:u.is_staff, login_url=reverse_lazy('foo'))
def Courseboard(request):
    form = CourseForm()
    course = Course.objects.all()
    # print(form)
    context = {
        'form': form,
        'Course':course,
    }
    return render(request , 'Teacher/Courseboard.html' , context )
     
def edit_lecture(request , id ):
    item = Lecture.objects.get(id = id)
    form = LectureForm(instance=item)
    context = {
        'form' : form,
        'id':id,
        
        
    }
    return render(request , 'Teacher/Lecture_edit.html' , context )
         
def Course_edit(request , id ):
    item = Course.objects.get(id = id)
        
        
    form = CourseForm(instance=item)      



    context = {
        'form' : form,
        'id':id,
    }

    return render(request , 'Teacher/Course_edit.html' , context  )                         



def Addstudent(request):
    form = Student_detailForm()
    context = {
        'form':form
    }
    return render(request , 'Teacher/Addstudent.html' , context )
        
        
        
        



    

                            