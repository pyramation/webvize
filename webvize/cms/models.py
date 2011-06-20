from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
import os, settings

def get_upload_path(instance, filename):
    return os.path.join('icons', str(instance.id), filename)

def get_icon_path(instance, filename):
    return os.path.join('icons', str(instance.id), filename)

def get_avatar_path(instance, filename):
        return os.path.join('avatar', str(instance.id), filename)

class Page(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, null=True, blank=True)
    #icon = models.ImageField(upload_to=get_icon_path, blank=False)
    icon = models.ImageField(upload_to=get_icon_path, blank=True)
    description = models.CharField(max_length=255)
    content = models.TextField()

    categories = models.ManyToManyField('Category')
    files = models.ManyToManyField('UserFile')
    keywords = models.ManyToManyField('Keyword')

    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

# should we use imageField??
class UserFile(models.Model):
    owner = models.ForeignKey(User)
    file = models.FileField(upload_to=get_upload_path, blank=False)

class Keyword(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    parent = models.ForeignKey('Category', null=True, blank=True)
    name = models.CharField(max_length=100)

class Group(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    files = models.ManyToManyField(UserFile)

class PhotoGroup(Group):
    def __unicode__(self):
        return "photogroup"

class VideoGroup(Group):
    def __unicode__(self):
        return "videogroup"

class MediaGroup(Group):
    def __unicode__(self):
        return "mediagroup"

class Profile(models.Model):
    avatar = models.ImageField(upload_to=get_avatar_path, blank=False)
    last_login = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class PageForm(ModelForm):
    class Meta:
        model = Page
        exclude = ['owner', 'icon', 'categories', 'files', 'keywords']
