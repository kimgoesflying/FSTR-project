from django.http import JsonResponse


def index(request):
    return JsonResponse({"error": "Hello world!"})
