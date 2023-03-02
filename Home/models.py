from email import message
from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField


# Create your models here.
class query_form(models.Model):
    form_name = models.CharField(max_length=100,null=True)
    form_email = models.CharField(max_length=100,null=True)
    form_subject = models.CharField(max_length=100,null=True)
    form_message = models.CharField(max_length=1000,null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.form_subject


class slider(models.Model):
    slider_name = models.CharField(null=True , max_length = 50 )
    slider_img = models.ImageField(upload_to='static/slider', null=True ,max_length = 100)
    Details = RichTextField(blank=True , null=True)
    
    def __str__(self):
        return self.slider_name
    
    
class q_form(models.Model):
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField( max_length=254 , null=True) 
    phone = models.CharField(max_length=15 , null=True)
    message = models.CharField( max_length=500, null=True)
    subject = models.CharField(max_length=100,null=True)
       
       
class email_data(models.Model):
    email = models.EmailField( max_length=254 , null=True)       
    def __str__(self):
        return self.email


class blog(models.Model):
    blog_title = models.CharField(max_length=300, null=True)
    blog_img = models.ImageField(blank=True, upload_to='media')
    blog_desp = RichTextField()
    blog_date = models.DateField(auto_now_add=False)
    blog_author = models.CharField(max_length=30,null=True)
    blog_slug = AutoSlugField(populate_from='blog_title',unique=True ,default=None, blank=False, null=True)

class Course(models.Model):
    course_img = models.ImageField(upload_to='media', blank=False)
    course_bann = models.ImageField(upload_to='media', blank=False,null=True)
    course_price = models.CharField(max_length=6, null=True)
    course_title = models.CharField(max_length=50,null=True, blank=False)
    course_descp = RichTextField(blank=False, null=False)
    course_stu = models.CharField(max_length=5,null=True)
    course_lessons = models.CharField(max_length=4, null=True)
    course_slug = AutoSlugField(populate_from='course_title',unique=True ,default=None, blank=False, null=True)

class StuReview(models.Model):
    stu_name = models.CharField(max_length=40, null=True)
    stu_descp = models.CharField(max_length=500,null=True)

class Event(models.Model):
    event_title = models.CharField(max_length=200,null=True, blank=False)
    event_img = models.ImageField(upload_to='media', blank=False)
    event_descp = RichTextField(blank=False, null=False)
    event_date = models.DateField(auto_now_add=False)
    event_time = models.TimeField(auto_now_add=False)
    event_location = models.CharField(max_length=30,null=True)
    event_slug = AutoSlugField(populate_from='event_title',unique=True ,default=None, blank=False, null=True)