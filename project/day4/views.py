from django.shortcuts import render, HttpResponse


def set_cookie(request):

    response = HttpResponse("OK")
    # uzupełniamy odpowiedź http o żądanie ustawienia ciasteczka User (wartość John)
    response.set_cookie('User', 'John')

    return response


def show_cookie(request):
    cookies = request.COOKIES
    user = cookies.get("User")

    return HttpResponse(user)


def delete_cookie(request):
    response = HttpResponse("OK")
    # uzupełniamy odpowiedź http o żądanie usunięcia ciasteczka
    response.delete_cookie("User")

    return response
