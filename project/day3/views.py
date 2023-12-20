from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt


def first_view(request):

    data = request.GET
    start = data.get('start')
    end = data.get('end')

    if start is None or end is None:
        return HttpResponse("Brak wymaganych parametrów (start, end)", status=400)

    response = ""
    for item in range(int(start), int(end)):
        response += f" {item}"

    # ew. list comprehension
    # response = " ".join([str(item) for item in range(int(start), int(end))])

    return HttpResponse(response)


@csrf_exempt
def third_view(request):
    if request.method == "GET":
        response = """
        <form method="POST">
            <input type="text" name="first_name" placeholder="first name">
            <input type="text" name="last_name" placeholder="last name"> 
            <input type="submit">
        </form>
        """
        return HttpResponse(response)

    elif request.method == "POST":
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        if first_name and last_name:
            return HttpResponse(f"Witaj, {first_name} {last_name}")
        else:
            return HttpResponse("Brak wymaganych parametrów (first_name, last_name)", status=400)


@csrf_exempt
def forth_view(request):
    if request.method == "GET":

        response = """
        <form action="" method="POST">
            <label>
                Temperatura:
                <input type="number" min="0.00" step="0.01" name="degrees">
            </label>
            <input type="submit" name="convertionType" value="celcToFahr">
            <input type="submit" name="convertionType" value="FahrToCelc">
        </form>
        """
        return HttpResponse(response)

    elif request.method == "POST":
        print(request.POST)
        data = request.POST

        degrees = data.get('degrees')
        convertion = data.get('convertionType')

        if convertion == "celcToFahr":
            result = float(degrees) * 9/5 + 32
        else:
            result = (float(degrees) - 32) * 5/9

        return HttpResponse(result)

