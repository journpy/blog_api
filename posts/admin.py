from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'blogger', 'content', 'date_created', 'date_updated',
        )
    search_fields = ('title',)
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.blogger = request.user
        super().save_model(request, obj, form, change)

