from rest_framework import permissions



class IsBloggerOrAuthenticatedReadOnly(permissions.BasePermission):
    message = 'Authenticated users can view but not edit the blog. Only the writer of the blog has read/write privileges.'
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    

    def has_object_permission(self, request, view, obj):
        if obj.blogger == request.user:
            return True
        return False
