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

@login_required(login_url='/signup')
def new_page(request):
    return render(request, 'home.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

## Face Detection

from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from mtcnn.mtcnn import MTCNN
from PIL import Image
import cv2
import numpy as np


def contrast(img):
    #img = cv2.imread(filename)
    Y = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #print(np.array(img))

    min = int(np.min(Y))
    max = int(np.max(Y))
    contrast = (max-min)/(max+min)
    return contrast

def face_detect(filename, faces,b):
    data=pyplot.imread(filename)
    pyplot.imshow(data)
    ax=pyplot.gca()

    for face in faces:
        x,y,width,height=face["box"]
        box=(x,y,width,height)
        b.append(box)
        #print(b)
        rect=Rectangle((x,y),width,height,fill=False,color="red")
        ax.add_patch(rect)
        #for key,value in face['keypoints'].items():
         #   dot=Circle(value,radius=1.5,color="yellow")
          #  ax.add_patch(dot)

    pyplot.show()

def crop(b,filename):
    img=Image.open(filename)
    for bb in b:
        box=bb
        box=(box[0],box[1],box[2]+box[0],box[3]+box[1])
        c=img.crop(box) #(left,upper,right,lower)
        #print(c.size)
        #pyplot.imshow(c)
        c.save(f"IM/cropped_image{box[0]}.jpg")
        downscale(c)

def downscale(img):
    basewidth=100
    wpercent=(basewidth/float(img.size[0]))
    #print(wpercent)
    hsize=int((float(img.size[1])*float(wpercent)))
    img5=img.resize((basewidth,hsize),Image.ANTIALIAS)
    img5.save(f"IM/resized_image{img.size[0]}.jpg")
    #print(img5.size)

def image_process(request):
    filename="IMAGE/image1.jpg"
    img=pyplot.imread(filename)
    thresh=0.55
    b=[]
    if(contrast(img) >= thresh):    #contrast checking
        print("Low Contrast: No")
        detector=MTCNN()            #face detection
        faces=detector.detect_faces(img)
        face_detect(filename, faces,b)
        #print(b)
        crop(b,filename)                     #cropping
    else:
        print("Low Contrast: Yes")
        pass
    return render(request)
