from django.db import models
from django.contrib.auth.models import AbstractUser ,User


# Create your models here.

'''
class UserInfo(AbstractUser):
    username = models.CharField(max_length = 100,null = False,unique = True)
    email = models.CharField(max_length = 200, null = False,unique = True)
    password = models.CharField(max_length = 200, null = False)
    

    def __Str__(self):
        return self.title
'''
class Blog(models.Model):
    blog_title = models.CharField(max_length = 1024)
    blog_date = models.DateField(auto_now_add=True,null = True,blank = True)
    blog_data = models.TextField(blank = True)
    blog_likes = models.IntegerField(blank = True,null = True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL,blank = True, null = True)
    image = models.ImageField(null = True,blank = True,upload_to = "images/")
    author_name = models.CharField(max_length = 1024,blank = True)


        

class Comments(models.Model):
    comment = models.TextField(blank=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)


