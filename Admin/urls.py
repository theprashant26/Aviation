from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Admin import Lectureview, views ,Revanueview
from Admin.views import Home
#from django.conf.urls import url
app_name = "Admin"

urlpatterns = [
    path('', views.Home , name='Home'),
    path('AHome', views.Home , name='AHome'),
    # lecture
    path('Lectureboard', Lectureview.Lectureboard , name='Lectureboard'),
    path('Addlecture', Lectureview.Lectures , name="Addlecture"),
    path('Lecture_edit/<int:id>/', Lectureview.Lecture_edit , name='Lecture_edit'),
    path('Leature_delete/<int:id>/', Lectureview.Leature_delete , name='Leature_delete'),
    # lecture
    
    # course
    path('Courseboard', views.Courseboard , name='Courseboard'),
    path('Addcourse', views.Addcourse , name='Addcourse'),
    path('Course_edit/<int:id>/', views.Course_edit , name='Course_edit'),
    path('Course_delete/<int:id>/', views.Course_delete , name='Course_delete'),
    # course
    
    # add teacher
    path('Addteacher', views.Addteacher , name='Addteacher'),
    path('Addteacherdetail', views.Addteacherdetail , name='Addteacherdetail'),
    # add teacher
    
    path('AdminProfile', views.Profile , name='AdminProfile'),
    path('Revenue', Revanueview.Revenue , name="Revenue"),
    path('paymentlist', Revanueview.paymentlist , name="paymentlist"),
    path('duelist', Revanueview.duelist , name="duelist"),

    # add student
    
    path('Studentboard', views.Studentboard , name="Studentboard"),
    path('Student_edit/<int:id>/', views.Student_edit , name="Student_edit"),
    path('Student_delete/<int:id>/', views.Student_delete , name="Student_delete"),
    path('Addstudent', views.Addstudent , name="Addstudent"),
    path('ADDstudent', views.ADDstudent , name="ADDstudent"),
    
    # path('Recheck', views.Student_Admission_recheck , name='Recheck' ),
    # add student
    
    # revenue
    # path('Revenue',revenueviews.revenue,name='Revenue'),
    # path('Todays_Revenue',revenueviews.Todays_Revenue,name='Todays_Revenue'),
    # path('totalrevenue',revenueviews.totalrevenue,name='totalrevenue'),
    
   

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
