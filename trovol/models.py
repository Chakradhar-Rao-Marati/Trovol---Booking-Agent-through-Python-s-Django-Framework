from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=50,default='default name')
    desc = models.TextField(default='default description')
    img = models.ImageField(upload_to='pics', height_field=None, width_field=None, max_length=None, default=' default img.jpg') 
    price = models.IntegerField(default= 0)
    sub = models.TextField(default='default subject')