from django.http import JsonResponse
from rest_framework.views import exception_handler


from rest_framework.views import APIView


def custom_exception_handler(exc, context):
    """
    Call REST framework's default exception handler first,
    to get the standard error response.
    """
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response


def custom_404(request, exception):
    """Custom 404 error."""
    return JsonResponse(
        {
            'error': 'Not Found', 
            'message': 'Your request was not found.', 
            'status_code': 404
            }, 
            status=404
            )


def custom_500(request):
    """Custom 500 error."""
    return JsonResponse({'error': 'Internal Server Error', 'message': 'The server encountered an error and could not complete your request.', 'status_code': 500}, status=500)
