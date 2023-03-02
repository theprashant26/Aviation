from django.contrib import admin
from django.urls import path

from Student import views
from accounts import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from .forms import MyPasswordResetForm,MySetPasswordForm
# from Student import views
from accounts import views

app_name = "accounts"

urlpatterns = [
    # path('', views.Student_Admission  ) ,
    # path('accounts/', views.signup  ) ,
    # path('signup/' ,views.signup, name='signup'),
    path('login/' ,views.login, name='login'),
    path('logout/' ,views.logout, name='logout'),
    path('password-reset1/' ,views.password_reset_request, name='password-reset1'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
    
]