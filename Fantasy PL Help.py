from operator import truediv
from turtle import left, right
import requests, json
from pprint import pprint
import pandas as pd
from tqdm.auto import tqdm


pd.set_option("display.max_rows", 999)
pd.set_option("display.max_columns", 999)
pd.set_option('display.width', 1000)

def get_gameweek_history(player_id):
    r = requests.get(
        base_url + 'element-summary/' +str(player_id) + '/'
    ).json()
    
    df = pd.json_normalize(r['history'])
    return df

base_url = 'https://fantasy.premierleague.com/api/'

r = requests.get(base_url+'bootstrap-static/').json()

# pprint(r, indent=2, depth=1, compact=True)

players = pd.json_normalize(r['elements'])
teams = pd.json_normalize(r['teams'])
positions = pd.json_normalize(r['element_types'])

players = players[
    ['id', 'first_name', 'second_name', 'web_name', 'team',
     'element_type']
]

players = players.merge(
    teams[['id','name']],
    left_on='team',
    right_on='id',
    suffixes=['_player', None]
).drop(['team','id'], axis=1)

players = players.merge(
    positions[['id', 'singular_name_short']],
    left_on='element_type',
    right_on='id'
).drop(['element_type', 'id'], axis=1)

tqdm.pandas()

points = players['id_player'].progress_apply(get_gameweek_history)

points = pd.concat(df for df in points)
points = players[['id_player', 'web_name']].merge(
    points,
    left_on='id_player',
    right_on='element'
)

print(points.groupby(
    ['element','web_name']
).agg(
    {'total_points': 'sum', 'goals_scored': 'sum', 'assists' : 'sum', 'minutes': 'sum', 'total_points': 'mean'}
).reset_index(
).sort_values(
    'total_points', ascending=False
).head(15))

