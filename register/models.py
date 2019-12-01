from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Users(models.Model):
    username = models.CharField(max_length=100)
    userid = models.CharField(max_length=15)
    mobile = models.CharField(max_length=12)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)