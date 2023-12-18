from django.urls import path, re_path

from hello.views import (
    hello, hello_george, hello_adam, hello_name
)


urlpatterns = [
    path('', hello),
    path('george/', hello_george),
    path('adam/', hello_adam),
    path('<str:name>/', hello_name)
]
