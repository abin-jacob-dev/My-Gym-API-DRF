from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    ROLES = [("member", "Member"), ("admin", "Owner")]
    role = models.CharField(max_length=20, choices=ROLES, default="member")
    phone = models.CharField(max_length=13, blank=True)

    def is_owner(self):
        return self.role == 'admin'
    def is_member(self):
        return self.role =='member'

class Student(models.Model):
    name  = models.CharField( max_length=50)
    age = models.IntegerField()
    place = models.CharField( max_length=50)