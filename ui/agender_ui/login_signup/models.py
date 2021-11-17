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
