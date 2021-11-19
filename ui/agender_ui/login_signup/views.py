from matplotlib import pyplot
import numpy as np
import cv2
from PIL import Image
from mtcnn.mtcnn import MTCNN
from matplotlib.patches import Circle
from matplotlib.patches import Rectangle
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
import tensorflow as tf
from django.templatetags.static import static
import io
import base64
# import requests

# Create your views here.


def age_model():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Conv2D(
        64, 3, activation='relu', input_shape=(200, 200, 3)))
    model.add(tf.keras.layers.MaxPool2D())
    model.add(tf.keras.layers.Conv2D(128, 3, activation='relu'))
    model.add(tf.keras.layers.MaxPool2D())
    model.add(tf.keras.layers.Conv2D(256, 3, activation='relu'))
    model.add(tf.keras.layers.MaxPool2D())
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(1024, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.1))
    model.add(tf.keras.layers.Dense(512, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.1))
    model.add(tf.keras.layers.Dense(512, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.1))
    model.add(tf.keras.layers.Dense(20, activation='softmax'))
    model.compile(optimizer='sgd',
                  loss=tf.losses.SparseCategoricalCrossentropy(
                      from_logits=False),
                  metrics=['accuracy'])
    model.load_weights('./models/checkpoint')
    return model


model = age_model()


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email_id = request.POST.get('email_id')
        password = request.POST.get('password')
        try:
            uid = User.objects.get(username=email_id)
            print(uid)
            return redirect('login')
        except User.DoesNotExist:
            user = User.objects.create_user(username=email_id,
                                            password=password, first_name=name)
            return redirect('login')

    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        email_id = request.POST.get('email_id')
        password = request.POST.get('password')
        user = authenticate(request, username=email_id, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('new_page')
        elif user is None:
            return redirect('signup')
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

@ login_required(login_url='/signup')
def new_page(request):
    return render(request, 'home.html')


def logout(request):
    auth_logout(request)
    return redirect('login')


def contrast(img):
    # img = cv2.imread(filename)
    Y = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # print(np.array(img))

    min = int(np.min(Y))
    max = int(np.max(Y))
    contrast = (max-min)/(max+min)
    return contrast


def face_detect(filename, faces, b):
    data = pyplot.imread(filename)
    # pyplot.imshow(data)
    ax = pyplot.gca()

    for face in faces:
        x, y, width, height = face["box"]
        box = (x, y, width, height)
        b.append(box)
        # print(b)
        rect = Rectangle((x, y), width, height, fill=False, color="red")
        ax.add_patch(rect)
        # for key,value in face['keypoints'].items():
        #   dot=Circle(value,radius=1.5,color="yellow")
        #  ax.add_patch(dot)

    # pyplot.show()


def crop(b, filename):
    img = Image.open(filename)
    for bb in b:
        box = bb
        box = (box[0], box[1], box[2]+box[0], box[3]+box[1])
        c = img.crop(box)  # (left,upper,right,lower)
        # print(c.size)
        # pyplot.imshow(c)
        c.save(f"IM/cropped_image{box[0]}.jpg")
        downscale(c)


def downscale(img):
    # basewidth = 100
    # wpercent = (basewidth/float(img.size[0]))
    # print(wpercent)
    # hsize = int((float(img.size[1])*float(wpercent)))
    img5 = img.resize((200, 200), Image.ANTIALIAS)
    img5.save("IM/resized_image.jpg")
    # print(img5.size)

@csrf_exempt
@ login_required(login_url='/signup')
def webcam(request):
    if request.method == 'POST':
        filename = './IMAGE/image.jpeg'
        with Image.open(io.BytesIO(base64.decodebytes(bytes(request.POST['img'].replace('data:image/jpeg;base64,', ''), "utf-8")))) as image:
            image.save(filename)
        img = pyplot.imread(filename)
        thresh = 0.55
        b = []
        if(contrast(img) >= thresh):  # contrast checking
            # print("Low Contrast: No")
            detector = MTCNN()  # face detection
            faces = detector.detect_faces(img)
            face_detect(filename, faces, b)
            # print(b)
            crop(b, filename)  #
            # model = age_model()
            test_image = tf.expand_dims(tf.io.decode_image(
                tf.io.read_file("IM/resized_image.jpg"), dtype=tf.float32), axis=0)
            prediction = np.argmax(model.predict(test_image)[0]) * 5
            message = f'Predicted Age: {prediction + 1}-{prediction + 5}'
            print('Prediction Complete')
        else:
            # print("Low Contrast: Yes")
            message = "Low Contrast Image. Please change you surroundings."
    else:
        message = ''
    return render(request, 'webcam.html', {'message': message})


@ login_required(login_url='/signup')
def builder(request):
    return render(request, 'builder.html')


@ login_required(login_url='/signup')
def form(request):
    return render(request, 'form.html')


# @ login_required(login_url='/signup')
# def webcam(request):
#     if request.method == 'POST':
#         print(request.POST.get('img'))
#     return render(request, 'webcam.html')


@ csrf_exempt
def save_form(request):
    if request.method == 'POST':
        pass
