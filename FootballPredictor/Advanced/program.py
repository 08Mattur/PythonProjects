from datetime import datetime, timedelta, date
import math
import pandas as pd
import numpy as np
from basic_prediction import basic_prediction

date_format = "%Y-%m-%d"

def read():
    df = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/E0.csv")
    df2= pd.read_csv("https://www.football-data.co.uk/mmz4281/2021/E0.csv")
    df3 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/E1.csv")
    df4= pd.read_csv("https://www.football-data.co.uk/mmz4281/2021/E1.csv")

    raw_df = pd.concat([df, df2, df3, df4])
    raw_df = raw_df[["Div", "Date", "HomeTeam", "AwayTeam", "Referee", "FTHG", "FTAG", "HC", "HS", "HST", "HF", "HY", "HR", "AC", "AS", "AST", "AF", "AY", "AR"]]
    raw_df['DateUpdated'] = pd.to_datetime(raw_df['Date'], format="%d/%m/%Y")
    raw_df = raw_df.sort_values(by=['DateUpdated'], ascending=False)
    return raw_df

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

pl_data = read()

start_date = date(2021, 8, 10)
#end_date = date(2021, 8, 15)
end_date = date(2022, 5, 10)

counter = 0
correct_result = 0
correct_btts = 0
home_counter = 0

current_result_streak = 0
highest_result_streak = 0
current_btts_streak = 0
highest_btts_streak = 0

for single_date in daterange(start_date, end_date):
    # print(single_date.strftime("%Y-%m-%d"))
    matches = pl_data[(pl_data['DateUpdated'] == single_date.strftime(date_format)) & (pl_data['Div'] == "E0")]
    
    for index, row in matches.iterrows():
        homeTeam = row["HomeTeam"]
        awayTeam = row["AwayTeam"]
        counter += 1

        predictions = basic_prediction(pl_data, homeTeam, awayTeam, single_date, date_format, row)
        correct_result += predictions[0]
        correct_btts += predictions[1]
        home_counter += predictions[2]

        current_result_streak = (current_result_streak + 1) * predictions[0]
        if current_result_streak > highest_result_streak:
            highest_result_streak = current_result_streak

        current_btts_streak = (current_btts_streak + 1) * predictions[1]
        if current_btts_streak > highest_btts_streak:
            highest_btts_streak = current_btts_streak

print("Games: " + str(counter))
print('')
print("Correct Predictions: " + str(correct_result))
print("Percentage: " + str(round((correct_result/counter)*100, 2)) + "%")
print('')
print("Correct BTTS Predictions: " + str(correct_btts))
print("Percentage: " + str(round((correct_btts/counter)*100, 2)) + "%")
print('')
print("Highest Result Streak: " + str(highest_result_streak))
print("Highest BTTS Streak: " + str(highest_btts_streak))
print('')
print("Home Wins: " + str(home_counter))
print("Percentage: " + str(round((home_counter/counter)*100, 2)) + "%")

    

