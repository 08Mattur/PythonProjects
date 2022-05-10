import math
import pandas as pd

def get_prediction(match, home_df, away_df):
    homeTeam = match[0]
    awayTeam = match[1]

    print(homeTeam + ' Vs ' + awayTeam)

    home_df = home_df[home_df['Team'] == homeTeam].head(10)
    away_df = away_df[away_df['Team'] == awayTeam].head(10)

    home_goals = home_df['Goals'].mean()
    home_goals_conceded = home_df['GoalsConceded'].mean()

    away_goals = away_df['Goals'].mean()
    away_goals_conceded = away_df['GoalsConceded'].mean()

    home_prediction = math.floor(home_goals * away_goals_conceded)
    away_prediction = math.floor(away_goals * home_goals_conceded)

    print(str(home_prediction) + ' - ' + str(away_prediction))

    home_games_scored_percent = len(home_df[home_df['Goals'] > 0])*10
    home_games_conceded_percent = len(home_df[home_df['GoalsConceded'] > 0])*10
    away_games_scored_percent = len(away_df[away_df['Goals'] > 0])*10
    away_games_conceded_percent = len(away_df[away_df['GoalsConceded'] > 0])*10

    home_goal_probability = ((home_games_scored_percent + away_games_conceded_percent)/2/100)
    away_goal_probability = ((away_games_scored_percent + home_games_conceded_percent)/2/100)

    btts_probability = home_goal_probability * away_goal_probability

    print("BTTS: " + str(round(btts_probability * 100,2)) + "%")
    print("BTTS ODDS: " + str(round(1/btts_probability, 2)))

    print('---------')

    print('Last 10 games averages')
    print('---------')
    # INDIVIDUAL AVERAGES
    print(homeTeam)
    print('Goals: ' + str(home_df['Goals'].mean()))
    print('Shots: ' + str(home_df['Shots'].mean()))
    print('SOT: ' + str(home_df['ShotsOnTarget'].mean()))
    print('Fouls: ' + str(home_df['Fouls'].mean()))
    print('Corners: ' + str(home_df['Corners'].mean()))
    print('Yellows: ' + str(home_df['Yellows'].mean()))
    print('Reds: ' + str(home_df['Reds'].mean()))
    print('ShotsAgainst: ' + str(home_df['ShotsConceded'].mean()))
    print('SOTAgainst: ' + str(home_df['ShotsOnTargetConceded'].mean()))
    print('CornersAgainst: ' + str(home_df['CornersConceded'].mean()))
    print('GoalsAgainst: ' + str(home_df['GoalsConceded'].mean()))

    print('---------')
    print(awayTeam)
    print('Goals: ' + str(away_df['Goals'].mean()))
    print('Shots: ' + str(away_df['Shots'].mean()))
    print('SOT: ' + str(away_df['ShotsOnTarget'].mean()))
    print('Fouls: ' + str(away_df['Fouls'].mean()))
    print('Corners: ' + str(away_df['Corners'].mean()))
    print('Yellows: ' + str(away_df['Yellows'].mean()))
    print('Reds: ' + str(away_df['Reds'].mean()))
    print('ShotsAgainst: ' + str(away_df['ShotsConceded'].mean()))
    print('SOTAgainst: ' + str(away_df['ShotsOnTargetConceded'].mean()))
    print('CornersAgainst: ' + str(away_df['CornersConceded'].mean()))
    print('GoalsAgainst: ' + str(away_df['GoalsConceded'].mean()))
    
    print('---------')

def get_all_predictions(matches, home_df, away_df):
    for match in matches:
        homeTeam = match[0]
        awayTeam = match[1]

        print(homeTeam + ' Vs ' + awayTeam)

        home_df_temp = home_df[home_df['Team'] == homeTeam].head(10)
        away_df_temp = away_df[away_df['Team'] == awayTeam].head(10)

        home_goals = home_df_temp['Goals'].mean()
        home_goals_conceded = away_df_temp['GoalsConceded'].mean()

        away_goals = away_df_temp['Goals'].mean()
        away_goals_conceded = away_df_temp['GoalsConceded'].mean()

        home_prediction = math.floor(home_goals * away_goals_conceded)
        away_prediction = math.floor(away_goals * home_goals_conceded)

        print(str(home_prediction) + ' - ' + str(away_prediction))

        home_games_scored_percent = len(home_df_temp[home_df_temp['Goals'] > 0])*10
        home_games_conceded_percent = len(home_df_temp[home_df_temp['GoalsConceded'] > 0])*10
        away_games_scored_percent = len(away_df_temp[away_df_temp['Goals'] > 0])*10
        away_games_conceded_percent = len(away_df_temp[away_df_temp['GoalsConceded'] > 0])*10

        home_goal_probability = ((home_games_scored_percent + away_games_conceded_percent)/2/100)
        away_goal_probability = ((away_games_scored_percent + home_games_conceded_percent)/2/100)

        btts_probability = home_goal_probability * away_goal_probability

        print("BTTS: " + str(round(btts_probability * 100,2)) + "%")
        print("BTTS ODDS: " + str(round(1/btts_probability, 2)))

        print('---------')

    


# HEAD TO HEAD
    # full_df = pd.concat([home_df, away_df])
    # full_df = full_df[full_df['Team'] == homeTeam]
    # full_df = full_df[full_df['Opponent'] == awayTeam]
    # print(full_df)