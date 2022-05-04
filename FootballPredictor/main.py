from reader import read_ds
from get_matches import get_matches

import pandas as pd
import math

ds = read_ds()

home_df = ds[0]
away_df = ds[1]

matches = get_matches()
print(matches)

for x in matches:
    homeTeam = x[0]
    awayTeam = x[1]

    print(homeTeam + ' Vs ' + awayTeam)

    home_goals = home_df.loc[home_df['Team'] == homeTeam].head(10)['Goals'].mean()
    home_goals_conceded = home_df.loc[home_df['Team'] == homeTeam].head(10)['GoalsConceded'].mean()

    away_goals = away_df.loc[away_df['Team'] == awayTeam].head(10)['Goals'].mean()
    away_goals_conceded = away_df.loc[away_df['Team'] == awayTeam].head(10)['GoalsConceded'].mean()

    home_prediction = math.floor(home_goals * away_goals_conceded)
    away_prediction = math.floor(away_goals * home_goals_conceded)

    print(str(home_prediction) + ' - ' + str(away_prediction))
    print('BTTS: ' + str(home_prediction > 0 and away_prediction > 0))
    print('---------')

    # print('Goals: ' + str(home_df.loc[home_df['Team'] == homeTeam].head(10)['Goals'].mean()))
    # print('Shots: ' + str(home_df.loc[home_df['Team'] == homeTeam].head(10)['Shots'].mean()))
    # print('SOT: ' + str(home_df.loc[home_df['Team'] == homeTeam].head(10)['ShotsOnTarget'].mean()))
    # print('Fouls: ' + str(home_df.loc[home_df['Team'] == homeTeam].head(10)['Fouls'].mean()))
    # print('Corners: ' + str(home_df.loc[home_df['Team'] == homeTeam].head(10)['Corners'].mean()))
    # print('Yellows: ' + str(home_df.loc[home_df['Team'] == homeTeam].head(10)['Yellows'].mean()))
    # print('Reds: ' + str(home_df.loc[home_df['Team'] == homeTeam].head(10)['Reds'].mean()))
    # print('ShotsAgainst: ' + str(home_df.loc[home_df['Team'] == homeTeam].head(10)['ShotsConceded'].mean()))
    # print('SOTAgainst: ' + str(home_df.loc[home_df['Team'] == homeTeam].head(10)['ShotsOnTargetConceded'].mean()))
    # print('CornersAgainst: ' + str(home_df.loc[home_df['Team'] == homeTeam].head(10)['CornersConceded'].mean()))
    # print('GoalsAgainst: ' + str(home_df.loc[home_df['Team'] == homeTeam].head(10)['GoalsConceded'].mean()))

    # print('-------')

    # print('Goals: ' + str(away_df.loc[away_df['Team'] == awayTeam].head(10)['Goals'].mean()))
    # print('Shots: ' + str(away_df.loc[away_df['Team'] == awayTeam].head(10)['Shots'].mean()))
    # print('SOT: ' + str(away_df.loc[away_df['Team'] == awayTeam].head(10)['ShotsOnTarget'].mean()))
    # print('Fouls: ' + str(away_df.loc[away_df['Team'] == awayTeam].head(10)['Fouls'].mean()))
    # print('Corners: ' + str(away_df.loc[away_df['Team'] == awayTeam].head(10)['Corners'].mean()))
    # print('Yellows: ' + str(away_df.loc[away_df['Team'] == awayTeam].head(10)['Yellows'].mean()))
    # print('Reds: ' + str(away_df.loc[away_df['Team'] == awayTeam].head(10)['Reds'].mean()))
    # print('ShotsAgainst: ' + str(away_df.loc[away_df['Team'] == awayTeam].head(10)['ShotsConceded'].mean()))
    # print('SOTAgainst: ' + str(away_df.loc[away_df['Team'] == awayTeam].head(10)['ShotsOnTargetConceded'].mean()))
    # print('CornersAgainst: ' + str(away_df.loc[away_df['Team'] == awayTeam].head(10)['CornersConceded'].mean()))
    # print('GoalsAgainst: ' + str(away_df.loc[away_df['Team'] == awayTeam].head(10)['GoalsConceded'].mean()))
