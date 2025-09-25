from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from posts.models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsBloggerOrAuthenticatedReadOnly, IsStaffOnly

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    """Post Viewset"""
    #permission_classes = [IsBloggerOrAuthenticatedReadOnly]
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    """User ViewSet"""
    #permission_classes = [IsStaffOnly]
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer






















