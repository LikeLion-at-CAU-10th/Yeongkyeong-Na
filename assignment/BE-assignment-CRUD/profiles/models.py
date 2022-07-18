from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=40,null=True,blank=True)
    message = models.CharField(max_length=90,null=True,blank=True)
    thumbnail = models.ImageField(upload_to="family/",null=True,blank=True)
    
class Profile(models.Model):
    family = models.ForeignKey('Family',on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20,null=True,blank=True)
    age = models.IntegerField(default=0,null=True,blank=True)
    phone = models.CharField(max_length=11,null=True,blank=True)
    pup_date = models.DateTimeField(auto_now_add=True)

