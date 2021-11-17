from django.conf.urls import url
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.middleware.csrf import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
import hashlib
from django.db.models import F
from django.contrib.auth.decorators import login_required
import uuid
import traceback
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# import requests

# Create your views here.


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email_id = request.POST.get('email_id')
        password = request.POST.get('password')
        # password = hashlib.sha256(post.password.encode())
        # password = post.password.hexdigest()
        user = User.objects.create_user(username=email_id,
                                        password=password, first_name=name)
        return redirect('login')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        print("Hello")
        email_id = request.POST.get('email_id')
        password = request.POST.get('password')
        user = authenticate(request, username=email_id, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('new_page')
    else:
        return render(request, 'login.html')


# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         passw = request.POST.get('password')

#         passw = hashlib.sha256(passw.encode())
#         passw = passw.hexdigest()
#         retrieved_pass = Users.objects.get(email_id=email).password
#         try:
#             retrieved_pass = Users.objects.get(email_id=email).password
#             print(Users.objects.get(email_id=email)._id)
#             if retrieved_pass != passw:
#                 return HttpResponse('Incorrect Password')
#         except:
#             return HttpResponse("Error ig")
#         try:
#             if Users.objects.filter(email_id__exact=email).get(password__exact=passw):
#                 objectId = Users.objects.get(email_id=email)._id
#                 # request.session._id = objectId
#                 # print(request.session['uid'])
#                 Users.objects.filter(
#                     email_id__exact=email).update(no_of_attempts=0)
#                 x = request.session.session_key
#                 if not x:
#                     request.session.create()
#                 request.session._id = objectId
#                 return redirect('new_page')
#         except Users.DoesNotExist:
#             Users.objects.filter(email_id__exact=email).update(
#                 no_of_attempts=F('no_of_attempts') + 1)
#             try:
#                 if Users.objects.filter(email_id__exact=email).get(no_of_attempts=3):
#                     new = hashlib.sha256(
#                         'temp_disabled_to_reset_password'.encode())
#                     Users.objects.filter(email_id__exact=email).update(
#                         password=new.hexdigest())
#                     return redirect('signup')
#             except:
#                 pass
#             return render(request, 'login.html')

#     else:
#         return render(request, 'login.html')

@login_required(login_url='/signup')
def new_page(request):
    return render(request, 'home.html')


def logout(request):
    auth_logout(request)
    return redirect('login')
