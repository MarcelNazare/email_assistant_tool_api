from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Draft(models.Model):
    recepient = models.CharField(max_length=100)
    
    text = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)