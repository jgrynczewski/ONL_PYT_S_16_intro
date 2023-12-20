from django.shortcuts import render, HttpResponse


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
