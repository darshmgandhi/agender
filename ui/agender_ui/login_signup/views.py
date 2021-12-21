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
from .detectors import age_model, gender_model, contrast, face_detect, crop
# import requests

# Create your views here.

model, prediction_age = age_model()
model_gender = gender_model()

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


@csrf_exempt
@ login_required(login_url='/signup')
def webcam(request):
	if request.method == 'POST':
		filename = './IMAGE/image.jpeg'
		with Image.open(io.BytesIO(base64.decodebytes(bytes(request.POST['img'].replace('data:image/jpeg;base64,', ''), "utf-8")))) as image:
			image.save(filename)
		#filename = './IMAGE/image1.jpeg'
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
			prediction = prediction_age[np.argmax(model.predict(test_image)[0])]
			prediction_gender = np.argmax(model.predict(test_image)[0])
			if prediction_gender == 0:
				prediction_gender = 'Male'
			else:
				prediction_gender = 'Female'
			message = f'Predicted Age: {prediction}, Predicted Gender: {prediction_gender}'
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
def form(request, id):
	# print(request.user)
	form_stuff = Form.objects.get(id=id)
	fields = form_stuff.fields
	# print(f1)
	return render(request, 'form.html', {'fields': fields})


# @ login_required(login_url='/signup')
# def webcam(request):
#     if request.method == 'POST':
#         print(request.POST.get('img'))
#     return render(request, 'webcam.html')


# @ csrf_exempt
# def save_form(request):
#     if request.method == 'POST':
#         pass

@csrf_exempt
def save_formdata(request):
	if request.method == 'POST':
		form_ = Form()
		form_.name = 'Form'
		form_.username = str(request.user)
		fields_ = []
		labels_ = []
		# user_id = str(request.user)
		# fields_.append({'user_id': user_id})
		for i in request.POST:
			values = request.POST[i].split(',')
			tag = values[-1]
			name_ = values[:-1]
			print("name", name_)
			for index,value in enumerate(name_):
				labels_.append({'label_name': value})
			fields_.append({'field_name': i, 'tag': tag, 'label': labels_})
			labels_ = []
		form_.fields = fields_
		print('SAVING')
		form_.save()
	return redirect('new_page')

@ csrf_exempt
def save_form(request):
	if request.method == 'POST':
		# first_name = form.cleaned_data['first_name']
		# last_name = form.cleaned_data['last_name']
		# email = form.cleaned_data['email']
		# p = response(first_name=first_name, last_name=last_name, email=email)
		# p.save()
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		title = request.POST['title']
		#vehicle = request.POST['vehicle']
		#print(request.POST['first_name'])
		p = response(first_name=first_name, last_name=last_name, email=email, title=title)
		p.save()

	return render(request, 'home.html', {'form': p})
