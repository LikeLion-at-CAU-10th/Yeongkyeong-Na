from django.db import models

# Create your models here.
class Likelion(models.Model):
    PART_CHOICES = (
        ('기획', "기획"),
        ('백엔드', "백엔드"),
        ("프론트엔드", "프론트엔드")
    )

    ROLE_CHOICES = (
        ("운영진","운영진"),
        ("멤버","멤버")
    )

    name = models.CharField(max_length=31, default="", unique=True)
    part = models.CharField(max_length=31, choices=PART_CHOICES, default="백엔드")
    role = models.CharField(max_length=31, choices=ROLE_CHOICES, default="멤버")
    major = models.CharField(max_length=31, default="")
    