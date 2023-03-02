from unicodedata import name
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from  Home import views
from django.views.static import serve


app_name = "Home"

urlpatterns = [
    # path('Student_Admission', views.Student_Admission , name='Student_Admission'  ),
    path('', views.Home  ),
    path('Base', views.Home , name="Base" ),
    path('Home', views.Home , name="Home" ),
    path('email_Data', views.email_Data , name="email_Data" ),
    path('Online-Admission', views.Addstudent , name="Online-Admission" ),
    path('About-Us', views.About , name="About-Us" ),
    path('ContactUs', views.ContactUs , name="ContactUs" ),
    path('Term-and-condition', views.TAC , name="Term-and-condition" ),
    path('Refund-&-Cancellation', views.TAC2 , name="Refund-&-Cancellation" ),
    path('allcourse/', views.allcourse.as_view(), name='allcourse'),
    path('privacypolicy', views.privacypol , name="privacypolicy" ),	
    path('coursedetailview/<slug>', views.coursedetailview.as_view(), name='coursedetailview'),
    path('blogdetailview/<slug>', views.blogdetailview.as_view(), name='blogdetailview'),
    path('eventdetailview/<slug>', views.eventdetailview.as_view(), name='eventdetailview'),
    path('blogpage/',views.blogpage.as_view(),name='blogpage'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),


]
