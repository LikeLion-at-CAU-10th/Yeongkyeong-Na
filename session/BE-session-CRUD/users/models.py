from multiprocessing.sharedctypes import Value
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.

# class ServiceUserManager(UserManager):
#     def _create_user(self, username, email, password, **extra_fields):
#         if not username:
#             raise ValueError
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)

#     def create_user(self, username, email=None, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", False)
#         extra_fields.setdefault("is_superuser", False)
#         return self._create_user(username, email, password, **extra_fields)

#     def create_superuser(self, username, email=None, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)

#         return self._create_user(username, email, password, **extra_fields)
        

# class ServiceUser(AbstractUser):
#     phone = models.CharField(verbose_name="전화번호", max_length=11, default="01000000000")
