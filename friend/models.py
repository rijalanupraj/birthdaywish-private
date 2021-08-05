from django.db import models
import os
# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path1(instance, filename):
    id = instance.id
    user_name = instance.name.lower()
    name, ext = get_filename_ext(filename)
    final_filename = f'{user_name}1{ext}'
    return f"images/friend_pic/{final_filename}"


def upload_image_path2(instance, filename):
    id = instance.id
    user_name = instance.name.lower()
    name, ext = get_filename_ext(filename)
    final_filename = f'{user_name}2{ext}'
    return f"images/friend_pic/{final_filename}"


def upload_image_path3(instance, filename):
    id = instance.id
    user_name = instance.name.lower()
    name, ext = get_filename_ext(filename)
    final_filename = f'{user_name}3{ext}'
    return f"image/friend_pic/{final_filename}"


class Friend(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    short_intro = models.TextField(max_length=255)
    birthday_wish = models.TextField(max_length=255)
    dob = models.DateField()
    description = models.TextField(null=True, blank=True)
    importance_level = models.IntegerField(default=1)
    picture1 = models.ImageField(
        upload_to=upload_image_path1)
    picture2 = models.ImageField(
        upload_to=upload_image_path2, blank=True, null=True)
    picture3 = models.ImageField(
        upload_to=upload_image_path3, blank=True, null=True)
    facebook_handle = models.CharField(max_length=255, blank=True, null=True)
    twitter_handle = models.CharField(max_length=255, blank=True, null=True)
    github_handle = models.CharField(max_length=255, blank=True, null=True)
    instagram_handle = models.CharField(max_length=255, blank=True, null=True)
    youtube_handle = models.CharField(max_length=255, blank=True, null=True)
    linkedin_handle = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
