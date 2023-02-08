from django.db import models


# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    about = models.TextField(null=True)
    bio = models.CharField(max_length=300, null=True)
    job = models.CharField(max_length=300, null=True, default='not named')
    location = models.CharField(max_length=300, null=True, default='iran')
    sign_up_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    profile_picture = models.FileField(upload_to='images', default='images/profile.jpg', null=True)
    cover_picture = models.FileField(upload_to='images', default='images/profile-banner.jpg', null=True)
    followers_usernames = models.CharField(max_length=1000, null=False, default="username,")
    followings_usernames = models.CharField(max_length=1000, null=False, default="username,")

    def __str__(self): return f"{self.first_name} {self.last_name} ({self.username})"


class Post(models.Model):
    # author_username = models.CharField(max_length=300, default=None)
    # author_profile_picture_address = models.CharField(max_length=600, default=None)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts', null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='images', null=True, blank=True, default=None)

    def __str__(self):
        return f"id= {self.id} / author= {self.author.username}"
