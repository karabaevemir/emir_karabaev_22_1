from django.db import models

# Create your models here.


class Hashtag(models.Model):
    icon = models.ImageField()
    title = models.CharField(max_length=255)


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    rate = models.DecimalField(max_digits=10, decimal_places=1)
    hasgtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE, null=True)


