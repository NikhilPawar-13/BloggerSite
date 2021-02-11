from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

from rest_framework.decorators import api_view 
from rest_framework.decorators import permission_classes
from rest_framework.response import Response 
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated 
from .serializer import UserSerializer , BlogSerializers , CommentsSerializers
from .models import Blog ,Comments
from django.contrib.auth.hashers import make_password


# Create your views here.


@api_view(['GET'])
def apiOverView(request):
   
    api_urls = {
        'List':'/user-list',
        'User-Login' : 'user-login/<str:user_Id>/<str:password>/',
        'User-Blog-list' : 'user-blog-list/',        
        'Detail view':'/user-detail/<str:pk>/',
        'Create':'/user-create/',
        'User-Blog-Update':'user-Blog-update/<str:user_Id>/',
        'User-Blog-Delete':'user-Blog-delete/<str:user_Id>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def UserList(request):
    users = User.objects.all()
  
    serializer = UserSerializer(users,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def UserLogin(request,user_Id,password):
    users = User.objects.all()     
    flag = False
    for user in users:
        if(user.user_Id == user_Id and user.password == password):
            flag = True
            break;
    if(flag == True):
        return Response("Login Sussess")
    else:
        return Response("Login failed")



@api_view(['POST'])
def UserCreate(request):
    print("***********************************")
    print(request.data)
    print("*********************************************")
    password = make_password(request.data['password'])
    print(password)
    data1 = {'username':request.data['username'],'email':request.data['email'],'password':password}
    print(data1)
    serializer = UserSerializer(data = data1)
    #tempData = User.objects.all()   
    #flag = True
    if serializer.is_valid():
        '''
        print(serializer.data)
        for object in tempData:
            if(serializer.data.get('user_Id') == object.user_Id and serializer.data.get('emsil') == object.emsil ):
                print("user already exist")
                flag = False
                break;
        if(flag == True):
            serializer.save()
        '''
        serializer.save()    


    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def UserBlogList(request):
    '''blogs = Blog.objects.filter(author = Id)'''
    blogs = Blog.objects.all()
    serializer = BlogSerializers(blogs,many = True)
    return Response(serializer.data)
    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def UserBlogCreate(request):
    
    serializer = BlogSerializers(data=request.data)
    
   
    if serializer.is_valid():       
        serializer.save()      

    return Response(serializer.data)
#Auth2O

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def UserBlogDelete(request,user_Id):
    try:
        blog = Blog.objects.get(pk = user_Id)
        print("----------------------------------------------")
        print(blog)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    blog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def UserBlogUpdate(request,user_Id):
    try:
        blog = Blog.objects.get(pk = user_Id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BlogSerializers(blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def UserId(request,username):
    
    user = User.objects.all()
    serializer = UserSerializer(user,many = True)
    return Response(serializer.data)

   


