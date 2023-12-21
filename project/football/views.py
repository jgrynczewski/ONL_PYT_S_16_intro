from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def add_game(request):
    if request.method == "GET":
        teams = Team.objects.all()
        response = """
            <form method=POST>
                <p><select name=team_home_id required>
        """

        for team in teams:
            response += f"<option value={team.id}>{team.name}</option>"
        response += """
            </select>
            <input type=number name=team_home_goals min=0 required></p>
        """

        response += """
                    <p><select name=team_away_id required>
            """

        for team in teams:
            response += f"<option value={team.id}>{team.name}</option>"
        response += """
                </select>
                <input type=number name=team_away_goals min=0 required></p>
                <input type=submit>
            </form>
        """

        return HttpResponse(response)

    elif request.method == "POST":
        data = request.POST
        team_home_id = data.get('team_home_id')
        team_home_goals = data.get('team_home_goals')
        team_away_id = data.get('team_away_id')
        team_away_goals = data.get('team_away_goals')

        if not team_home_id or not team_home_goals or not team_away_id or not team_away_goals:
            return HttpResponse("Brak wymaganych parametrów", status=400)

        team_home = Team.objects.get(id=team_home_id)
        team_away = Team.objects.get(id=team_away_id)

        # Tworzymy wpis w bazie danych w tabeli game
        Game.objects.create(
            team_home=team_home,
            team_home_goals=team_home_goals,
            team_away=team_away,
            team_away_goals=team_away_goals
        )

        # Zad 4 - punktacja
        if team_home_goals > team_away_goals:
            team_home.points += 3
            team_home.save()
        elif team_away_goals > team_home_goals:
            team_away.points += 3
            team_away.save()
        else:
            team_home.points += 1
            team_away.points += 1
            team_home.save()
            team_away.save()

        return redirect(f'/games/?id={team_home_id}')


def set_as_favourite(request):
    data = request.GET
    team_id = data.get('id')

    # sprawdzamy czy parametr metody get - id - istnieje oraz czy ma poprawną wartość
    if not team_id or not team_id.isdigit():
        return HttpResponse("Błędna wartość parametru", status=400)  # 400 - bad request

    # sprawdzamy, czy w bazie istnieje wpis w tabelce Team dla wskazanej wartości parametru id
    if not Team.objects.filter(id=team_id).exists():
        return HttpResponse("Klub o wskazanym id nie istnieje", status=404)  # 400 - bad request

    response = HttpResponse(f"Przeglądarka zapisuje ciasteczko fav_team z wartością {team_id}")
    response.set_cookie('fav_team', team_id)

    return response
