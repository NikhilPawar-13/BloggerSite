from rest_framework import serializers
from . models import Blog ,Comments
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model =  User
        fields = ('username','email','password')

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '_all__'





