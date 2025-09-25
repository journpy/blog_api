from rest_framework import serializers

from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'posts',)


class PostSerializer(serializers.ModelSerializer):
    blogger = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False, read_only=False)
    class Meta:
        model = Post
        fields = (
            'title', 
            'blogger', 
            'content', 
            'date_created',
            'date_updated',
            )
        

