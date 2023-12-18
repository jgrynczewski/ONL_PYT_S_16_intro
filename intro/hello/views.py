from django.shortcuts import HttpResponse


def hello(request):
    return HttpResponse("Hello, world!")


def hello_george(request):
    return HttpResponse("Hello, George!")


def hello_adam(request):
    return HttpResponse("Hello, Adam!")


def hello_name(request, name):
    return HttpResponse(f"Hello, {name}!")
