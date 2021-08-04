from django.db import models

# Create your models here.


class Friend(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    short_intro = models.TextField(max_length=255)
    birthday_wish = models.TextField(max_length=255)
    dob = models.DateField()
    description = models.TextField(null=True, blank=True)
    importance_level = models.IntegerField(default=1)
    picture1 = models.ImageField(upload_to="images/profile_pic")
    picture2 = models.ImageField(
        blank=True, null=True, upload_to="images/profile_pic")
    picture3 = models.ImageField(
        blank=True, null=True, upload_to="images/profile_pic")
    facebook_handle = models.CharField(max_length=255, blank=True, null=True)
    twitter_handle = models.CharField(max_length=255, blank=True, null=True)
    github_handle = models.CharField(max_length=255, blank=True, null=True)
    instagram_handle = models.CharField(max_length=255, blank=True, null=True)
    youtube_handle = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
