import random

from django.shortcuts import render, HttpResponse


# Create your views here.
def random_view(request):
    num = random.randint(0, 100)
    return HttpResponse(f"Wylosowano liczbę: {num}")


def random_view2(request, max_number):
    num = random.randint(0, int(max_number))
    msg = f"Użytkownik podał wartość {max_number}. Wylosowano liczbę: {num}."
    return HttpResponse(msg)


def random_view3(request, min_number, max_number):
    num = random.randint(int(min_number), int(max_number))
    msg = f"Użytkownik podał wartości {min_number} - {max_number}. Wylosowano liczbę: {num}."
    return HttpResponse(msg)
