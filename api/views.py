from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from posts.models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsBloggerOrAuthenticatedReadOnly, IsStaffOnly
from django_filters import rest_framework as filtering 
from rest_framework import filters

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    """Post Viewset"""
    #permission_classes = [IsBloggerOrAuthenticatedReadOnly]
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filtering.DjangoFilterBackend]
    filterset_fields = ['title', 'content']


class UserViewSet(viewsets.ModelViewSet):
    """User ViewSet"""
    #permission_classes = [IsStaffOnly]
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']






















