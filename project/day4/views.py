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


def set_session(request):
    request.session['counter'] = 0
    return HttpResponse("OK")


def show_session(request):
    if 'counter' not in request.session:
        return HttpResponse("Brak sesji lub w danych sesji brak klucza counter")

    request.session['counter'] += 1
    counter = request.session['counter']

    return HttpResponse(counter)


def delete_session(request):
    del request.session['counter']

    return HttpResponse("Usunięto klucz counter z sesji")


@csrf_exempt
def login(request):
    if request.method == "GET":

        response = ""

        logged_user = request.session.get('loggedUser')
        if logged_user:
            response += f"<h2>Witaj {logged_user}</h2>"

        response += """
        <form action="" method="POST">
            <label>
                Imię:
                <input type="text" name="name">
            </label>
            <input type="submit">
        </form>
        """

        return HttpResponse(response)

    elif request.method == "POST":
        data = request.POST
        name = data.get('name')

        if not name:
            return HttpResponse("Brak wymaganych parametrów", status=400)

        request.session['loggedUser'] = name

    return HttpResponse("OK")


@csrf_exempt
def add_to_session(request):
    if request.method == "GET":
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

    elif request.method == "POST":
        data = request.POST
        key = data.get('key')
        value = data.get('value')

        if not key or not value:
            return HttpResponse("Brak wymaganych parametrów", status=400)

        request.session[key] = value

        return HttpResponse(f"Stworzono wpis {key} o wartości {value} w sesji.")


def show_all_session(request):
    response = ""
    print(dir(request.session))
    for key, value in request.session.items():
        response += f"<p>{key} = {value}</p>"

    return HttpResponse(response)
