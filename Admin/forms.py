from cProfile import label
from dataclasses import fields
from pyexpat import model
from xml.dom.minidom import Attr
from django.core import validators
from django import forms
from .models import  Course, UserProfile , ckeditor_test
# from django import ModelForm
from django.forms import ModelForm, PasswordInput
from ckeditor.fields import RichTextField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Select, Textarea, TextInput, NumberInput , FileField


class newuserform(UserCreationForm):
    class Meta:
        model = User
        # fields = '__all__'
        bsclass = 'form-control'
        fields = ['username', 'password1','password1', 'first_name' ,'is_staff']
        widgets = {
            'username':TextInput(attrs={ 'class': bsclass,'type':'email' }),
            'password1':PasswordInput(attrs={'class': bsclass,'type':'password'  }),
            'password1':PasswordInput(attrs={'class': bsclass,'type':'password'  }),
            'first_name':TextInput(attrs={ 'class': bsclass,'type':'email' }),
        }

class UserProfileform(forms.ModelForm):
    class Meta:
        model = UserProfile
        bsclass = 'form-control'
        
        fields = ['phone','about']
        widgets = {
            'phone':TextInput(attrs={ 'class': bsclass,'type':'phone' }),
            'about':TextInput(attrs={ 'class': bsclass,'type':'text' }),
            
            
        }
        

# class ckeditor_test_Form(forms.ModelForm):
#     class Meta:
#         model = ckeditor_test
#         fields = ['post']
        

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
    
        widgets = {
            'Course_name': TextInput(attrs={'class': 'form-control mb-3'}),
            'Price': TextInput(attrs={'class': 'form-control mb-3'}),
            'title': TextInput(attrs={'class': 'form-control mb-3'}),
            'sub_title': TextInput(attrs={'class': 'form-control mb-3'}),
            # 'Thumb': ModelForm(attrs={'class': 'form-control mb-3'}),
            'Duration': Select(attrs={'class': 'form-select mb-3'}),
            
            'Details': Textarea(attrs={'class': 'form-control mb-3'}),
            

        }


# class Student_detail_editForm(forms.ModelForm):
#     class Meta:
#         cls_sty = 'gridsys p-2 mb-4 col-4'
#         model = Student_detail
#         # fields = ['Name','Email', 'Number' ,'Number2'   , 'Aadhaar' , 'Aadhaar' , 'Gender', 'Father' , 'Education', 'Course_name' , 'doc_10',  'State' , 'City' , 'House' ,'Post_office' ,'Block','District' ,'Pincode' , 'Locality'   ]
#         fields = '__all__'

#         widgets = { 
#              'Name' : forms.TextInput(attrs={'class': cls_sty ,'placeholder':'Name'}),
#              'Email' : forms.TextInput(attrs={'class': cls_sty , 'readonly': 'True', 'type' : 'email' , 'placeholder':'Email'}),
#              'Number' : forms.TextInput(attrs={'class': cls_sty ,'type':'phone', 'placeholder':'Number'}),
#             #  'Number2' : forms.TextInput(attrs={'class': cls_sty ,'type':'phone' ,'placeholder':'Alternate No.'}),
           

#          }
        
    
   