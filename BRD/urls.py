"""Admission URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
# import notifications.urls

from django.conf.urls import include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from Admin import views
admin.site.site_header = 'Student Admission'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include( 'Home.urls')),
    path('',include( 'Student.urls')),
    path('',include( 'Teacher.urls')),
    path('',include( 'Admin.urls')),
    path('accounts/',include ('accounts.urls')),
    path('robots.txt',TemplateView.as_view(template_name="Base/robots.txt", content_type="text/plain")),
    path(r'^$',views.handler404, name='handler404'),
    #url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    # url('', include('social_django.urls', namespace='social')),
    #  path('forest', include('django_forest.urls')),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
    # url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404= 'Admin.views.handler404'