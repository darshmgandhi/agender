from django.shortcuts import render, redirect
from .models import *
from django.http import HttpRequest, HttpResponse, JsonResponse
import json
from django.middleware.csrf import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
import hashlib
from django.db.models import F
import uuid
import traceback
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login, logout
# import requests

# Create your views here.


def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        post = Users()
        post.name = request.POST.get('name')
        post.email_id = request.POST.get('email_id')
        post.password = request.POST.get('password')
        post.password = hashlib.sha256(post.password.encode())
        post.password = post.password.hexdigest()
        post.uid = uuid.uuid4().hex[:8]
        post.save()
        return redirect('new_page')
    else:
        return render(request, 'signup.html')

    return render(request, "signup.html")


def new_page(request):
    return HttpResponse("Logged in.")
