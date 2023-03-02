from urllib import request
from django.test import TestCase

from Admin.models import UserProfile

# Create your tests here.
def MakeOTP():
    import random,string
    a = 'TITAN/'
    b = str(''.join(random.choices( string.digits, k = 6)))
    
    print(a+b)
    
MakeOTP()
# We are glad that you have enrolled the course. Here is the link to reset your password. You can continue to learn course video content and material by sign-in with your registered username and password.

