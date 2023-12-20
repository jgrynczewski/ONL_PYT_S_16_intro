from django.shortcuts import render, HttpResponse

from football.models import Team

def league_table(request):

    teams = Team.objects.all().order_by('-points')
    response = ''
    for idx, team in enumerate(teams, start=1):
        response += f"{idx} {team.name} {team.points}"
        response += "<br/>"

    return HttpResponse(response)
