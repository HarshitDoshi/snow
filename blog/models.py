from django.db import models
from django.utils import timezone
import datetime


class BlogOwner(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=256)
    email = models.EmailField()
    authors_list = 



class Blog(models.Model):
    def __str__(self):
        return self.title

    owner = models.ForeignKey


class BlogPost(models.Model):
    def __str__(self):
        return self.post_id + ' : ' + self.title


    def user_directory_path(self, instance, filename):
        return '{0}/banner_images/%Y/%m/%d/{1}/{2}/'.format(instance.user, instance.post_id, filename)


    user = models.CharField('User', max_length=1024)
    post_id = models.AutoField('Post ID', primary_key=True, unique=True)
    title = models.CharField('Title', max_length=1024)
    date_of_publication = models.DateTimeField('Date Published')
    banner_image = models.ImageField('Banner Image', upload_to=user_directory_path)
    author = models.CharField('Author', max_length=1024)
    objects = models.Manager()
