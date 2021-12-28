from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('new_page', views.new_page, name="new_page"),
    #path('image_process', views.image_process, name="image_process"),
    path('builder', views.builder, name='builder'),
    path('form/<int:id>', views.form, name='form'),
    path('download/<int:id>', views.download, name='download'),
	path('', views.new_page, name="new_page"),
    path('webcam/<int:id>', views.webcam, name='webcam'),
    path('save_form/<int:id>', views.save_form, name = 'save_form'),
    path('save_formdata', views.save_formdata, name = 'save_formdata'),
    path('form_delete/<int:id>', views.form_delete, name = 'form_delete')
]
