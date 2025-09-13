from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from posts.models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsBloggerOrAuthenticatedReadOnly

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    """Post Viewset"""
    permission_classes = [IsBloggerOrAuthenticatedReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    """User ViewSet"""
    permission_classes = [permissions.IsAdminUser,]
    queryset = User.objects.all()
    serializer_class = UserSerializer






















