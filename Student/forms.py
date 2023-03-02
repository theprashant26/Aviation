from xml.dom.minidom import Attr
from django import forms
from Student.models import Student_detail
from django.forms import ModelForm, Select, Textarea, TextInput, NumberInput, DateField
from datetime import datetime

class Student_detailForm(forms.ModelForm):
    class Meta:
        cls_sty = 'form-control  '
        model = Student_detail
        fields = ['Name', 'Email',  'Number', 'DOB', 'Aadhaar', 'Gender', 'Education', 'doc_10th', 'doc_12th', 'doc_Graduate',
                  'doc_postgraduate', 'Course_name', 'Address',  'State',  'District', 'Pincode']

        # fields = '__all__'
        label = {
            'Gender': 'Gender',
            'Date': 'Date'
        }
        widgets = {
            'Name': forms.TextInput(attrs={'class': cls_sty, 'type': 'text','placeholder': 'Name','pattern':"[a-zA-Z'-'\s]*"}),
            'Email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Email'}),
            'Number': forms.TextInput(attrs={'class': cls_sty, 'type': 'number','placeholder':'Mobile No.','onKeyPress':"if(this.value.length==10) return false;" }),
            #  'Number2' : forms.TextInput(attrs={'class': cls_sty ,'type':'phone' ,'placeholder':'Alternate No.'}),
            'Gender': Select(attrs={'class': 'form-control', 'type': 'choice'}),
            'DOB': forms.DateInput(attrs={'class': cls_sty,
                                          'type': 'date',
                                          'max' : datetime.now().date()
                                          }),
            'Education': Select(attrs={'class': 'form-control ', 'type': 'choice'}),

            'Aadhaar': forms.TextInput(attrs={'class': cls_sty, 'type': 'number','placeholder': 'Aadhaar No.','onKeyPress':"if(this.value.length==12) return false;"}),
            'Course_name': Select(attrs={'class': 'form-control', 'type': 'choice'}),
            
            'doc_10th': forms.FileInput(attrs={'class': cls_sty, 'type': 'file'}),
            'doc_12th': forms.FileInput(attrs={'class': cls_sty, 'type': 'file'}),
            'doc_Graduate': forms.FileInput(attrs={'class': cls_sty, 'type': 'file'}),
            'doc_postgraduate': forms.FileInput(attrs={'class': cls_sty, 'type': 'file'}),
	        'Address': forms.TextInput(attrs={'class': cls_sty, 'placeholder': 'Address'}),
            'State': Select(attrs={'class': 'form-control','type': 'choice' }),
            'City': forms.TextInput(attrs={'class': cls_sty}),
            'House': forms.TextInput(attrs={'class': cls_sty}),
            'Post_office': forms.TextInput(attrs={'class': cls_sty}),
            'Tehsil': forms.TextInput(attrs={'class': cls_sty}),
            'District': forms.TextInput(attrs={'class': cls_sty}),
            'Pincode': forms.TextInput(attrs={'class': cls_sty,'type': 'number','placeholder': 'Pin Code','onKeyPress':"if(this.value.length==6) return false;"}),
        }
        
