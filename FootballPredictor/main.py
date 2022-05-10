from reader import read_ds
from get_matches import get_matches
from get_prediction import get_prediction, get_all_predictions
from datetime import datetime

pl_only = False

def print_matches(matches):
    for match in matches:
        index = matches.index(match) +1
        print("For a " + match[0] + " VS " + match[1] + " Prediction, Type: '" + str(index) + "'")
        print('')
    print_help()

def print_help():
    print("Input 'X' To Exit")
    print("Input 'D' For New Date")
    print("Input 'S' For Summary Prediction")
    print("Input 'H' For Help")
    pl_string = "ON" if pl_only else "OFF"
    print("Premier League Only: " + pl_string + ". Input 'P' to toggle")

ds = read_ds()
home_df = ds[0]
away_df = ds[1]

x = 1
date_input = datetime.today().strftime("%Y-%m-%d")
user_input = "D"
matches = []
while x == 1:
    if user_input == "D":
        date_input = input("Input a date to check for fixtures (YYYY-MM-DD): ")
        print('')
        matches = get_matches(date_input, pl_only)
        print_matches(matches)

    user_input = input("Prediction: ")
    

    if user_input == "X":
        x += 1
    if user_input == "H":
        print_help()
    if user_input == "P":
        pl_only = not pl_only
        
    if user_input == "S":
        get_all_predictions(matches, home_df, away_df)
    
    if user_input.isnumeric() and int(user_input) < len(matches) +1:
        get_prediction(matches[int(user_input)-1], home_df, away_df)