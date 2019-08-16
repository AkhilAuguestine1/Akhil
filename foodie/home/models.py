from django.db import models
from datetime import datetime
import uuid
# Create your models here.

class user (models.Model):
    objects = models.Manager ()
    userid = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    question = models.IntegerField()
    answer = models.CharField(max_length=200)
    date_created = models.DateTimeField('date created', default=datetime.now())

    def _str_(self):
        return self.username
    
