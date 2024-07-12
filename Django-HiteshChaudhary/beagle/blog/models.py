from django.db import models
from django.utils import timezone

# Create your models here.

class Blogs(models.Model):
    Title = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='blog/')
    Description = models.TextField()
    Time = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.Title