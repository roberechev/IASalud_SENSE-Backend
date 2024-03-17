from django.http import HttpResponse

def prueba1(request):
    return HttpResponse("Hello, world. You're at the polls index.")