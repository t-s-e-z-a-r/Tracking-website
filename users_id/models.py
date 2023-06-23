from django.db import models
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# Create your models here.

class User_Url(models.Model):
    ID_User = models.CharField(max_length=255)

    def __str__(self):
        return self.ID_User

class Url(models.Model):
    user = models.ForeignKey(User_Url, on_delete=models.CASCADE)
    Url_User = models.CharField(max_length=255)

    def __str__(self):
        return self.Url_User