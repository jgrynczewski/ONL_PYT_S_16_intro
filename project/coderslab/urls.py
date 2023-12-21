"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from exercises_app import views
from football import views as football_views
from day3 import views as day3_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.article_view),

    path('show-band/<int:band_id>/', views.show_band),
    path('table/', football_views.league_table),
    path('games/', football_views.games_played),

    path('first/', day3_views.first_view),
    path('third/', day3_views.third_view),
    path('forth/', day3_views.forth_view),

    path('add-game/', football_views.add_game),
]
