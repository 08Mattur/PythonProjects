import requests
from bs4 import BeautifulSoup
from translate_team_name import translate_team_name

def get_matches(fixture_date, pl_only):    
    url = "https://www.bbc.com/sport/football/scores-fixtures/" + fixture_date

    a = requests.get(url)
    soup = BeautifulSoup(a.text, features="html.parser")

    games = []
    league_list = ['Premier League', 'League One', 'Champions League', 'Championship', 'Spanish La Liga', 'German Bundesliga', 'French Ligue 1', 'Italian Serie A', 'The FA Cup']

    if pl_only:
        league_list = ['Premier League']
    for league in soup.find_all(class_="qa-match-block"):
        for i in league.select('h3'):
            if any(i.text in s for s in league_list):
                for match in league.find_all(class_="sp-c-fixture__wrapper"):
                    teams = match.find_all(class_="qa-full-team-name")
                    home_team = teams[0].text
                    away_team = teams[1].text

                    home_team = translate_team_name(home_team)
                    away_team = translate_team_name(away_team)

                    games.append([home_team, away_team])
        
    return games