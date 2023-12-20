from django.shortcuts import render, HttpResponse

from exercises_app.models import Article, Band

# Create your views here.
def article_view(request):

    articles = Article.objects.filter(status=2)

    response = '<ul>'
    for article in articles:
        if not article.author is None:
            response += f"<li>{article.title} {article.author} {article.date_added}</li>"
        else:
            response += f"<li>{article.title} {article.date_added}</li>"
    response += '</ul>'

    return HttpResponse(response)


def show_band(request, band_id):

    band = Band.objects.get(id=band_id)
    response = f"{band.name} {band.get_genre_display()} {band.year} {band.still_active}"

    return HttpResponse(response)
