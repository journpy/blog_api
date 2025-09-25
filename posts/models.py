from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    """A post"""
    title = models.CharField(max_length=150)
    blogger = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='posts',
        )
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)




    class Meta:
        ordering = ('-date_created',)


    def __str__(self):
        """String representation of the model objects."""
        return self.title
