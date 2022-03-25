import requests
from bs4 import BeautifulSoup
import pandas as pd

def grab_epl_data():
    res = requests.get("http://www.football-data.co.uk/englandm.php")

    soup = BeautifulSoup(res.content, 'lxml')

    table = soup.find_all('table', {'align': 'center', 'cellspacing': '0', 'width': 800})[1]
    body = table.find_all('td', {'valign': 'top'})[1]
    
    links = [link.get('href') for link in body.find_all('a')]
    links_text = [link_text.text for link_text in body.find_all('a')]

    data_urls = []

    prefix = 'http://www.football-data.co.uk/'
    for i, text in enumerate(links_text):
        if text == 'Premier League':
            data_urls.append(prefix + links[i])

    data_urls = data_urls[:4]

    df = pd.DataFrame()
    for url in data_urls:
        season = url.split('/')[4]
        print(f"Getting season data {season}")

        temp_df = pd.read_csv(url)
        temp_df['season'] = season

        # Create helpful columns like Day, Month, Year, Date etc. so that our data is clean
        temp_df = (temp_df.dropna(axis='columns', thresh=temp_df.shape[0]-30)
                          .assign(Day=lambda df: df.Date.str.split('/').str[0],
                                  Month=lambda df: df.Date.str.split('/').str[1],
                                  Year=lambda df: df.Date.str.split('/').str[2])
                          .assign(Date=lambda df: df.Month + '/' + df.Day + '/' + df.Year)
                          .assign(Date=lambda df: pd.to_datetime(df.Date))
                          .dropna())
        df = df.append(temp_df, sort=True)
    df = df.dropna(axis=1).dropna().sort_values(by='Date')
    print('DataGet Finished')

    return df

df = grab_epl_data()
df.to_csv("D:\Python Projects\Betting\data\epl_data.csv", index= False)