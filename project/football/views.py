from django.shortcuts import render, HttpResponse

from football.models import Team, Game

def league_table(request):

    teams = Team.objects.all().order_by('-points')
    response = ''
    for idx, team in enumerate(teams, start=1):
        response += f"""
            {idx} 
            <a href="/games/?id={team.id}">{team.name}</a> 
            {team.points}
        """
        response += "<br/>"

    return HttpResponse(response)


def games_played(request):
    data = request.GET
    team_id = data.get('id')

    if team_id is None:
        return HttpResponse("Brak wymaganych parametrów (id)", status=400)

    team = Team.objects.get(id=team_id)
    home_games = Game.objects.filter(team_home=team)
    away_games = Game.objects.filter(team_away=team)

    games = home_games | away_games

    response = ""
    for game in games:
        response += f"{game.team_home.name} || {game.team_away.name} ({game.team_home_goals}:{game.team_away_goals})"
        response += "</br>"

    return HttpResponse(response)
