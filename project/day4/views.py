from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def add_to_cookie(request):
    if request.method == "GET":  # wyświetlanie formularza
        response = """
            <form action="#" method="POST">
                <label>
                    Klucz:
                    <input type="text" name="key">
                </label>
                <label>
                    Wartość:
                    <input type="text" name="value">
                </label>
                <input type="submit">
            </form>
        """

        return HttpResponse(response)

    elif request.method == "POST":  # obsługa danych formularza
        data = request.POST
        key = data.get('key')
        value = data.get('value')

        response = HttpResponse(f"Przeglądarka zapisuje ciasteczko {key}")
        response.set_cookie(key, value)

        return response
