"""
URL configuration for django1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from exercises_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('random/', views.random_view),
    path(
        'random/<int:max_number>/',
        views.random_view2
    ),
    # Zadanie 1 (Definiowanie urli ciąg dalszy)
    # re_path(
    #     r'^random/(?P<max_number>\d{2,4})/$',
    #     views.random_view2
    # ),

    path(
        'random/<int:min_number>/<int:max_number>/',
        views.random_view3
    ),
    # Zadanie 1 (Definiowanie urli ciąg dalszy)
    # re_path(
    #     'random/(?P<min_number>\d{2})/(?P<max_number>\d{4})/',
    #     views.random_view3
    # ),

]
