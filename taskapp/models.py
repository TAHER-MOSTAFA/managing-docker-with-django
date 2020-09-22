from django.db import models
from django.contrib.auth.models import User

    

class Docker(models.Model):
    ContainerName = models.CharField(max_length=30,unique=True)
    image = models.CharField(max_length=50)
    command = models.TextField(null=True,blank=True)
    cotainer_id = models.TextField(null=True,blank=True)
    status = models.CharField(default='Pending',max_length=20)
    user = models.ManyToManyField(User,related_name="instaces")