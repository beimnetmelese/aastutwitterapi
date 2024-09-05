from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Sex = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    profile = models.ImageField(upload_to="user/images",null=True, blank=True)
    bio = models.CharField(max_length= 255)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=1, choices=Sex, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Follow(models.Model):
    follow = models.ForeignKey(User, on_delete= models.CASCADE, related_name= "follow")
    follower = models.ForeignKey(User, on_delete= models.CASCADE, related_name= "follower")
    follow_date = models.DateTimeField(auto_now_add=True)
