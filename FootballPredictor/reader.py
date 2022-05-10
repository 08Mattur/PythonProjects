from datetime import datetime
import pandas as pd

def read_ds():
    df = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/E0.csv")
    df2= pd.read_csv("https://www.football-data.co.uk/mmz4281/2021/E0.csv")
    df3 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/SP1.csv")
    df4= pd.read_csv("https://www.football-data.co.uk/mmz4281/2021/SP1.csv")
    df5 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/E1.csv")
    df6= pd.read_csv("https://www.football-data.co.uk/mmz4281/2021/E1.csv")
    df7 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/F1.csv")
    df8= pd.read_csv("https://www.football-data.co.uk/mmz4281/2021/F1.csv")
    df9 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/D1.csv")
    df10= pd.read_csv("https://www.football-data.co.uk/mmz4281/2021/D1.csv")
    df11 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/I1.csv")
    df12= pd.read_csv("https://www.football-data.co.uk/mmz4281/2021/I1.csv")
    df13 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/E2.csv")
    df14= pd.read_csv("https://www.football-data.co.uk/mmz4281/2021/E2.csv")

    raw_df = pd.concat([df, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14])
    raw_df = raw_df[["Date", "HomeTeam", "AwayTeam", "Referee", "FTHG", "FTAG", "HC", "HS", "HST", "HF", "HY", "HR", "AC", "AS", "AST", "AF", "AY", "AR"]]
    raw_df['Date'] = pd.to_datetime(raw_df['Date'], format="%d/%m/%Y")
    raw_df = raw_df.sort_values(by=['Date'], ascending=False)

    # rename(columns={
    #     "FTHG" : "HomeGoals",
    #     "FTAG" : "AwayGoals",
    #     "HC" : "HomeCorners",
    #     "HS" : "HomeShots",
    #     "HST" : "HomeShotsOnTarget", 
    #     "HF" : "HomeFouls", 
    #     "HY" : "HomeYellows", 
    #     "HR" : "HomeReds", 
    #     "AC" : "AwayCorners", 
    #     "AS" : "AwayShots", 
    #     "AST" : "AwayShotsOnTarget", 
    #     "AF" : "AwayFouls", 
    #     "AY" : "AwayYellows", 
    #     "AR" : "AwayReds"
    # })

    raw_df.loc[raw_df['FTHG'] == raw_df['FTAG'], 'HResult'] = 'Draw'
    raw_df.loc[raw_df['FTHG'] > raw_df['FTAG'], 'HResult'] = 'Win'
    raw_df.loc[raw_df['FTHG'] < raw_df['FTAG'], 'HResult'] = 'Loss'

    raw_df.loc[raw_df['FTHG'] == raw_df['FTAG'], 'AResult'] = 'Draw'
    raw_df.loc[raw_df['FTHG'] > raw_df['FTAG'], 'AResult'] = 'Loss'
    raw_df.loc[raw_df['FTHG'] < raw_df['FTAG'], 'AResult'] = 'Win'

    home_df = raw_df[[
        'Date',
        'HomeTeam',
        'FTHG',
        'HS',
        'HST',
        'HF',
        'HC',
        'HY',
        'HR',
        'AwayTeam',
        'AS',
        'AST',
        'FTAG',
        'AC',
        'HResult'
    ]]

    home_df = home_df.rename(
        columns={
            'HomeTeam':'Team',
            'FTHG':'Goals',
            'HS':'Shots',
            'HST':'ShotsOnTarget',
            'HF':'Fouls',
            'HC':'Corners',
            'HY':'Yellows',
            'HR':'Reds',
            'AwayTeam' : 'Opponent',
            'AS':'ShotsConceded',
            'AST':'ShotsOnTargetConceded',
            'FTAG':'GoalsConceded',
            'AC':'CornersConceded',
            'HResult':'Result'
    })

    away_df = raw_df[[
        'Date',
        'AwayTeam',
        'FTAG',
        'AS',
        'AST',
        'AF',
        'AC',
        'AY',
        'AR',
        'HomeTeam',
        'HS',
        'HST',
        'FTHG',
        'HC',
        'AResult'
    ]]

    away_df = away_df.rename(
        columns={
            'AwayTeam':'Team',
            'FTAG':'Goals',
            'AS':'Shots',
            'AST':'ShotsOnTarget',
            'AF':'Fouls',
            'AC':'Corners',
            'AY':'Yellows',
            'AR':'Reds',
            'HomeTeam': 'Opponent',
            'HS':'ShotsConceded',
            'HST':'ShotsOnTargetConceded',
            'FTHG':'GoalsConceded',
            'HC':'CornersConceded',
            'AResult':'Result'
        })

    return [home_df.sort_values(by=['Date'], ascending=False), away_df.sort_values(by=['Date'], ascending=False)]