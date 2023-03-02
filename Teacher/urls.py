from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Teacher import views 

app_name = "Teacher"

urlpatterns = [
    # path('Profile', views.Profile , name='Profile'  ),
    path('TAddstudent', views.Addstudent , name='TAddstudent'  ),
    # leature
    path('TLectureboard', views.Lectureboard , name='TLectureboard'  ),
    path('TCourseboard', views.Courseboard , name='TCourseboard'),
    # leature
    #course 
    path('TLecture_edit/<int:id>/', views.edit_lecture , name='TLecture_edit'),
    path('TCourse_edit/<int:id>/', views.Course_edit , name='TCourse_edit'),
    #course 
    
    
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)