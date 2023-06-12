from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    content = models.TextField()
    date_of_post = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title