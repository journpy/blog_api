from rest_framework import permissions



class IsBloggerOrAuthenticatedReadOnly(permissions.BasePermission):
    message = """
    Authenticated users can view but not edit the blog. 
    Only the writer of the blog has read/write privileges.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    

    def has_object_permission(self, request, view, obj):
        if obj.blogger == request.user:
            return True
        return False


class IsStaffOnly(permissions.BasePermission):
    message = """Staff accounts can view the list of users but only super users can access a user details."""

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return False
