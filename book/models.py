from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name
class Auther(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Book(models.Model):
    name = models.CharField(max_length=50,unique=True)
    content = models.TextField(max_length=1000)
    publish_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='books/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    auther = models.ForeignKey(Auther,on_delete= models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['id']
