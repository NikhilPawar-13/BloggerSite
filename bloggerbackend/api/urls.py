from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('',views.apiOverView, name = 'api-overview'),
    path('user-list/',views.UserList, name = 'user-list'),
    path('user-create/',views.UserCreate, name = 'user-create'),
    path('user-login/<str:user_Id>/<str:password>/',views.UserLogin, name = 'user-login'),
    path('user-blog-list/',views.UserBlogList, name = 'user-blog-list'),
    path('user-blog-create/',views.UserBlogCreate, name = 'user-blog-create'),
    path('user-Id/<str:username>/',views.UserId , name = 'User-Id'),
    path('user-blog-update/<str:user_Id>/',views.UserBlogUpdate , name = 'User-blog-update'),
    path('user-blog-delete/<str:user_Id>/',views.UserBlogDelete , name = 'User-blog-delete'),
    path('get-token/',TokenObtainPairView.as_view(),name = 'token-obtain-pair'),
    path('refresh-token/',TokenRefreshView.as_view(), name = 'token-refresh'),
    path('verify-token/',TokenVerifyView.as_view(), name = 'token-verify'),
] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)