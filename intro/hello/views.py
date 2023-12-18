from django.shortcuts import HttpResponse


def hello(request):
    return HttpResponse("Hello, world!")


def hello_george(request):
    return HttpResponse("Hello, George!")
