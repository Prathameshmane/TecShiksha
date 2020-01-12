from django.db import models

# Create your models here.

class Blog(models.Model):
    heading = models.CharField(max_length = 100)
    img = models.ImageField(upload_to='blog_pics')
    content = models.TextField()

class Workshop(models.Model):
    heading = models.CharField(max_length = 100)
    img = models.ImageField(upload_to='blog_pics')
    date = models.CharField(max_length = 100)
    venue = models.TextField()
    site = models.CharField(max_length = 100)

class Offer(models.Model):
    name = models.CharField(max_length = 100)
    discount = models.IntegerField()
    on_offer = models.BooleanField(default=False)
