from turtle import TurtleGraphicsError
from django import forms
from django.db import models
from django.urls import reverse
# from ckeditor.fields import RichTextField
from ckeditor.fields import RichTextField
from django.utils import timezone
from datetime import date, datetime 
from django.contrib.auth.models import AbstractUser
# from django.db import models
#from django.utils.translation import ugettext_lazy as _
# from .managers import CustomUserManager
# add new teacher
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class newuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email', 'first_name' , 'last_name' , 'password1','password2','is_staff' ,    ]
        bsclass = 'form-control'
        widgets = {
            'username':  forms.TextInput(attrs={ 'class': bsclass,'type':'email' }),
            'email':  forms.TextInput(attrs={ 'class': bsclass,'type':'email' }),
            'first_name':  forms.TextInput(attrs={ 'class': bsclass,'type':'text' }),
            'last_name':  forms.TextInput(attrs={ 'class': bsclass,'type':'text' }),
        }  



class UserProfile(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   phone = models.CharField(max_length=14, blank=True, null=True)
   about = models.CharField(max_length=50, blank=True, null=True)
   def __str__(self):
        return self.user.username
#    gender = models.CharField(
#         max_length=10,  null=True)
# add new teacher

class ckeditor_test(models.Model):
    post = RichTextField(blank=True, null=True)

class courses_det(models.Model):
    course_img = models.ImageField(upload_to='static/course_img',null=True,max_length=100)
    course_details = RichTextField(blank=True , null=True)
    course_no = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.course_no

class slider(models.Model):
    slider_name = models.CharField(null=True , max_length = 50 )
    slider_img = models.ImageField(upload_to='static/slider', null=True ,max_length = 100)
    Details = RichTextField(blank=True , null=True)
    
    def __str__(self):
        return self.slider_name



class Course(models.Model):

    id = models.AutoField(primary_key=True)
    Course_name = models.CharField(max_length = 55 , null= True )
    Price = models.IntegerField(null=True)
    # Thumb = models.ImageField(upload_to='static/Admin/img', null=True ,max_length = 100)
    Details = RichTextField(blank=True , null=True)
    duration = {
        ('1 mon','1 MONTH'),
        ('3 mon','3 MONTH'),
        ('6 mon','6 MONTH'),
    }
    Duration = models.CharField(max_length=100,choices=duration,null=True)
    title = models.CharField(max_length=127)
    sub_title = models.CharField(max_length=127)
   
    is_official = models.BooleanField(default=False)
   

    
    def __str__(self):
        return self.title
   
    #new added   



# Create your models here.

    