from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're the polls index.")

# Create your views here.
