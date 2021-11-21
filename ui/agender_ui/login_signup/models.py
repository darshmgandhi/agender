from django.db import models
from django.utils import timezone
from django.db import models
from djongo import models


# class Users(models.Model):
#     # uid = models.CharField(db_column='Uid', primary_key=True, max_length=30)
#     _id = models.ObjectIdField()
#     email_id = models.TextField(
#         db_column='Email_id', unique=True)
#     password = models.TextField(db_column='Password')
#     name = models.TextField(db_column='Name')
#     no_of_attempts = models.IntegerField(db_column='No_of_attempts')

#     class Meta:
#         managed = False

class Field(models.Model):
    #_id = models.ObjectIdField()
    field_name = models.CharField(max_length = 30)
    tag = models.CharField(max_length = 30)
    label = models.CharField(max_length = 30)
    
    class Meta:
        abstract = True

class Form(models.Model):
    name = models.CharField(max_length = 100)
    fields = models.ArrayField(
        model_container = Field
    )

TITLE_TYPE_CHOICES = (('mr','Mr'), ('mrs','Mrs'), ('miss','Miss'),)
VEHICLE_TYPE_CHOICES = ( ('Bike','bike'), ('Car','car'), ('Cycle','cycle'))

class response(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    title = models.CharField(max_length=10, choices=TITLE_TYPE_CHOICES)
    #image = models.ImageField(upload_to='IMAGE/')
    #vehicle = models.CharField(max_length=50,widget=models.CheckboxSelectMultiple, choices=VEHICLE_TYPE_CHOICES)