from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Student import views
app_name = "Student"

urlpatterns = [
    path('SProfile', views.Profile , name='SProfile'  ),
    path('SProfile', views.Profile , name='SProfile'  ),
    path('Lecturevideo', views.Lecturevideo , name='Lecturevideo'  ),
    path('payment', views.payment , name='payment'  ),
    path('paymenthandler/', views.paymenthandler , name='paymenthandler'  ),
    path('paymentstatus', views.paymentstatus , name='paymentstatus'  ),
    path('invoice2/<int:id>/', views.invoice2 , name='invoice2'  ),
    
    # path('Student_Admission', views.Student_Admission , name='Student_Admission'  ),
    # path('Home', views.Student_Admission , name="Home" ),
    # path('Recheck', views.Student_Admission_recheck , name='Recheck' ),
    
    # path('Manage-Lecture',Lectureviews.Lecture_manage ,name='Manage-Lecture'),
    # path('Lecture_edit/<int:id>/',Lectureviews.Lecture_edit ,name='Lecture_edit'),

    # revenue
    # path('Revenue',revenueviews.revenue,name='Revenue'),
    # path('Todays_Revenue',revenueviews.Todays_Revenue,name='Todays_Revenue'),
    # path('totalrevenue',revenueviews.totalrevenue,name='totalrevenue'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)