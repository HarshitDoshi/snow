from django.db import models


class BlogPost(models.Model):
    def __str__(self):
        return self.post_id


    post_id = models.IntegerField()
    title = models.CharField(max_length=1024)
    date_of_publication = models.DateTimeField()
    objects = models.Manager()
    image = models.ImageField()


