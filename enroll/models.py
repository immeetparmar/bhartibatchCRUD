from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="post_images/", null=True, blank=True)
    
    def __str__(self):
       return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    college_name = models.CharField(max_length=50)

    def __str__(self):
       return self.name

