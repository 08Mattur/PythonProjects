import pandas as pd
from collections import defaultdict

filePath = "D:\Python Projects\Betting\data\epl_data.csv"
df = pd.read_csv(filePath)

def getData(isHome, team):
    is_team = []
    if isHome == 1:
        is_team = df['HomeTeam'] == team

        team_df = df[is_team]
        team_data = [
            team_df['FTHG'].mean(),
            team_df['FTAG'].mean(),
            team_df['HTHG'].mean(),
            team_df['HTAG'].mean(),
            team_df['HC'].mean(),
            team_df['AC'].mean(),
            team_df['HS'].mean(),
            team_df['AS'].mean(),
            team_df['HST'].mean(),
            team_df['AST'].mean(),
            team_df['HF'].mean(),
            team_df['AF'].mean(),
            team_df['HY'].mean(),
            team_df['AY'].mean(),
            team_df['HR'].mean(),
            team_df['AR'].mean()
        ]

        return team_data
    else:
        is_team = df['AwayTeam'] == team
        team_df = df[is_team]
        team_data = [
            team_df['FTAG'].mean(),
            team_df['FTHG'].mean(),
            team_df['HTAG'].mean(),
            team_df['HTHG'].mean(),
            team_df['AC'].mean(),
            team_df['HC'].mean(),
            team_df['AS'].mean(),
            team_df['HS'].mean(),
            team_df['AST'].mean(),
            team_df['HST'].mean(),
            team_df['AF'].mean(),
            team_df['HF'].mean(),
            team_df['AY'].mean(),
            team_df['HY'].mean(),
            team_df['AR'].mean(),
            team_df['HR'].mean()
        ]

        return team_data

matrices = [
    'Goals', 
    'Goals Conceded', 
    'Goals 1st Half', 
    'Goals Conceded 1st Half', 
    'Corners', 
    'Corners Conceded', 
    'Shots', 
    'Shots Conceded', 
    'Shots On Target', 
    'Shots On Target Conceded',
    'Fouls Given',
    'Fouls Taken',
    'Yellow Cards Received',
    'Yellow Cards Given',
    'Red Cards Received',
    'Red Cards Given'
]

season_means = [
    df['FTHG'].mean(),
    df['FTAG'].mean(),
    df['HTHG'].mean(),
    df['HTAG'].mean(),
    df['HC'].mean(),
    df['AC'].mean(),
    df['HS'].mean(),
    df['AS'].mean(),
    df['HST'].mean(),
    df['AST'].mean(),
    df['HF'].mean(),
    df['AF'].mean(),
    df['HY'].mean(),
    df['AY'].mean(),
    df['HR'].mean(),
    df['AR'].mean()
]

season_totals = [
    df['FTHG'].sum(),
    df['FTAG'].sum(),
    df['HTHG'].sum(),
    df['HTAG'].sum(),
    df['HC'].sum(),
    df['AC'].sum(),
    df['HS'].sum(),
    df['AS'].sum(),
    df['HST'].sum(),
    df['AST'].sum(),
    df['HF'].sum(),
    df['AF'].sum(),
    df['HY'].sum(),
    df['AY'].sum(),
    df['HR'].sum(),
    df['AR'].sum()
]

home_data = getData(1, 'Liverpool')
away_data = getData(0, 'Aston Villa')

result_df = pd.DataFrame(list(zip(matrices, home_data, away_data, season_means, season_totals)), columns=['Matrices', 'Home', 'Away', 'Season Average', 'Season Totals'])
print(result_df)