from rest_framework import filters


class IsBloggerReadPostFilter(filters.BaseFilterBackend):
    """Custom filter to see posts belonginng to current user."""
    
    def filter_queryset(self, request, queryset, view):
        """Only return posts belonging to currently logged in user."""
        return queryset.filter(blogger=request.user)
