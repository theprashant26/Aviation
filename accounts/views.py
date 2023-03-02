# passwork reset
from BRD.settings import EMAIL_HOST_USER , EMAIL_HOST_USER2
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core import mail

# passwork reset
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib import messages
EMAIL_HOST_USER = EMAIL_HOST_USER2
# from Student.models import Student_detail


# def signup(request):
#     if request.method == "POST":
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 User.objects.get(username=request.POST['username'])
#                 return render(request, 'accounts/signup.html', {'error': 'Username is already taken!'})
#             except User.DoesNotExist:
#                 user = User.objects.create_user(
#                     request.POST['username'], password=request.POST['password1'])
#                 auth.login(request, user)
#                 return redirect('/')
#         else:
#             return render(request, 'accounts/signup.html', {'error': 'Password does not match!'})
#     else:
#         return render(request, 'accounts/signup.html')

import sweetify
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        # USERS = User.objects.filter(user , is_superuser=True).exists()
        if user is not None:
            auth.login(request, user)
            print(User.objects.all())
            # if not user.is_superuser and not user.is_staff:
            if request.user.is_superuser:
            # if user is user.is_superuser:
                sweetify.success(request, 'Hey ', text='Successfully Logged In', persistent='Done')

                return redirect('Admin:AdminProfile')
                # return redirect('/Recheck')
            elif request.user.is_staff:
                auth.login(request, user)
                return redirect('Admin:AdminProfile')
            else:
                # if Student_detail.objects.filter(Payment=True).exists():
                auth.login(request, user)
                # pass
                return redirect('Admin:AdminProfile')
                # else:
                #     return redirect('/Recheck')
        else:

            message = messages.warning(
                request, 'Username or password is incorrect!')
            # return render (request,'accounts/login.html', {'error':'Username or password is incorrect!'})
            return render(request, 'accounts/login.html', message)
    else:
        return render(request, 'accounts/login.html')


def logout(request):
        if request.method == 'POST':
            auth.logout(request)
            return redirect('Home:Base')
        else:
            return render(request, 'accounts/logout.html')


# passwork reset

def password_reset_request(request):
	if request.method == "POST":

		password_reset_form = PasswordResetForm(request.POST)

		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
            
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "accounts/password_reset_email.txt"
					c = {
					"email": user.email,
					'domain': request.META['HTTP_HOST'],
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						mail.send_mail(subject, email, EMAIL_HOST_USER, [
						          user.email], fail_silently=False)
                        # send_mail(subject, EMAIL_HOST_USER, [email], fail_silently = False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect("/accounts/password-reset/done/")

            

            # else:
                # pass           
	password_reset_form = PasswordResetForm()
            
	# return render(request=request, template_name="main/password/password_reset.html", context={"password_reset_form":password_reset_form})
	return render(request,"accounts/password_reset.html", context={"form":password_reset_form})