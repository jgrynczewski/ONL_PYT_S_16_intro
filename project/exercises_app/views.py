from django.shortcuts import render, HttpResponse

from exercises_app.models import Article

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
