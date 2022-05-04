import requests
from bs4 import BeautifulSoup

def get_matches():    
    url = "https://www.bbc.com/sport/football/scores-fixtures/"

    a = requests.get(url)
    soup = BeautifulSoup(a.text, features="html.parser")

    games = []
    league_list = ['Premier League', 'Champions League', 'Championship', 'Spanish La Liga', 'German Bundesliga', 'French Ligue 1', 'Italian Serie A']
    for league in soup.find_all(class_="qa-match-block"):
        for i in league.select('h3'):
            if any(i.text in s for s in league_list):
                for match in league.find_all(class_="sp-c-fixture__wrapper"):
                    teams = match.find_all(class_="qa-full-team-name")
                    home_team = teams[0].text
                    away_team = teams[1].text

                    if home_team == "Newcastle United":
                        home_team = "Newcastle"
                    elif home_team == "Norwich City":
                        home_team = "Norwich"
                    elif home_team == "Wolverhampton Wanderers":
                        home_team = "Wolves"
                    elif home_team == "Brighton & Hove Albion":
                        home_team = "Brighton"
                    elif home_team == "Leeds United":
                        home_team = "Leeds"
                    elif home_team == "Manchester City":
                        home_team = "Man City"
                    elif home_team == "Tottenham Hotspur":
                        home_team = "Tottenham"
                    elif home_team == "Leicester City":
                        home_team = "Leicester"
                    elif home_team == "West Ham United":
                        home_team = "West Ham"
                    elif home_team == "Manchester United":
                        home_team = "Man United"
                    elif home_team == "AFC Bournemouth":
                        home_team = "Bournemouth"
                    elif home_team == "Nottingham Forest":
                        home_team = "Nott'm Forest"

                    if away_team == "Newcastle United":
                        away_team = "Newcastle"
                    elif away_team == "Norwich City":
                        away_team = "Norwich"
                    elif away_team == "Wolverhampton Wanderers":
                        away_team = "Wolves"
                    elif away_team == "Brighton & Hove Albion":
                        away_team = "Brighton"
                    elif away_team == "Leeds United":
                        away_team = "Leeds"
                    elif away_team == "Manchester City":
                        away_team = "Man City"
                    elif away_team == "Tottenham Hotspur":
                        away_team = "Tottenham"
                    elif away_team == "Leicester City":
                        away_team = "Leicester"
                    elif away_team == "West Ham United":
                        away_team = "West Ham"
                    elif away_team == "Manchester United":
                        away_team = "Man United"
                    elif away_team == "AFC Bournemouth":
                        away_team = "Bournemouth"
                    elif away_team == "Nottingham Forest":
                        away_team = "Nott'm Forest"

                    games.append([home_team, away_team])
        
    return games