from django.urls import path

from hello.views import hello, hello_george

urlpatterns = [
    path('', hello),
    path('george/', hello_george),
]
