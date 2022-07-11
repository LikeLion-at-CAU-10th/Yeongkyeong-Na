from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=20,null=True,blank=True)
    age = models.IntegerField(default=0,null=True,blank=True)
    phone = models.CharField(max_length=11,null=True,blank=True)
    pup_date = models.DateTimeField(auto_now_add=True)

