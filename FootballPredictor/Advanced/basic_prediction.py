import math

def basic_prediction(pl_data, homeTeam, awayTeam, single_date, date_format, row):
    pred_avg = 7

    home_goal_avg = pl_data.loc[(pl_data['HomeTeam'] == homeTeam) & (pl_data['DateUpdated'] < single_date.strftime(date_format))]['FTHG'].head(pred_avg).mean()
    home_goal_conceded_avg = pl_data.loc[(pl_data['HomeTeam'] == homeTeam) & (pl_data['DateUpdated'] < single_date.strftime(date_format))]['FTAG'].head(pred_avg).mean()

    away_goal_avg = pl_data.loc[(pl_data['AwayTeam'] == awayTeam) & (pl_data['DateUpdated'] < single_date.strftime(date_format))]['FTAG'].head(pred_avg).mean()
    away_goal_conceded_avg = pl_data.loc[(pl_data['AwayTeam'] == awayTeam) & (pl_data['DateUpdated'] < single_date.strftime(date_format))]['FTHG'].head(pred_avg).mean()

    home_xG = math.floor(home_goal_avg * away_goal_conceded_avg)
    away_xG = math.floor(home_goal_conceded_avg * away_goal_avg)

    x_result = "draw"
    if home_xG > away_xG:
        x_result = "home"
    elif away_xG > home_xG:
        x_result = "away"

    x_btts = "no"
    if home_xG > 0 and away_xG > 0:
        x_btts = "yes"

    home_g = row["FTHG"]
    away_g = row["FTAG"]

    result = "draw"
    if home_g > away_g:
        result = "home"
    elif away_g > home_g:
        result = "away"

    btts = "no"
    if home_g > 0 and away_g > 0:
        btts = "yes"    

    correct_result = 0
    correct_btts = 0
    
    if x_result == result:
        correct_result = 1
    if x_btts == btts:
        correct_btts = 1

    # print(homeTeam + " V " + awayTeam)
    # print("Expected Score: " + str(home_xG) + " - " + str(away_xG))
    # print("Actual Score: " + str(home_g) + " - " + str(away_g))
    # print("-----")
    
    return [correct_result, correct_btts]