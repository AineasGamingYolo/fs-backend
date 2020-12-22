#from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.contrib.auth.models import UserManager


import json

class CustomUser(AbstractUser):
    # Basic info
    username = models.CharField(blank=True, unique=True, max_length=100)
    email = models.EmailField(blank=True, unique=True, max_length=100)
    password = models.CharField(blank=True, max_length=100)
    recovery_email = models.EmailField(blank=True, max_length=100)
    # Personal Info
    first_name = models.CharField(blank=True, max_length=100)
    last_name = models.CharField(blank=True, max_length=100)
    country = CountryField()

    objects = UserManager()

    def __str__(self):
        return self.username


class Thread(models.Model):
    title = models.CharField(blank=True, max_length=100)
    content = models.TextField(blank=True, max_length=3000)
    #comments = models.ManyToManyField(Comment)
    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField()
    thread_author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    objects = models.Manager()
    show_in_home = models.BooleanField(blank=True, null=True)
    auth_key = models.CharField(blank=True, max_length=64)
    slug = models.SlugField(max_length=32)


    class meta:
        app_label = 'threads_frontend_json_data'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')




class Comment(models.Model):
    content = models.TextField(blank=True, max_length=1500)
    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    comment_author = models.TextField(blank=True) #ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='comments')
    auth_key = models.CharField(blank=True, max_length=64)
    active = models.BooleanField(default=False)
    #def __str__(self):
    #    return self.author

    class meta:
        app_label = 'comments_frontend_json_data'

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.comment_author)