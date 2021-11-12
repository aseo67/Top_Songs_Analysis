# Code to scrape data from Spotify Charts website for United States Top 200 List
# https://spotifycharts.com/regional/us/daily/

# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

# Get list of dates to use in url strings
dates = []
start = dt.date(2021, 11, 1)
end = dt.date.today()
delta = end - start
for i in range(int(delta.days+1)):
    day = start + dt.timedelta(days=i)
    url_string = day.strftime("%Y-%m_%d")
    dates.append(url_string)

# Get list of full urls for each date
date_urls = []
for date in dates:
    url = "https://spotifycharts.com/regional/us/daily/"
    date_url = url+date
    date_urls.append(date_url)

# Define function to run scraping process
def scrape(date_urls):

    data = []

    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit URL
    url = "https://spotifycharts.com/regional/us/daily/"
    browser.visit(url)

    # Set up HTML parser
    html = browser.html
    song_soup = soup(html, 'html.parser')
    playlist = song_soup.find('table', class_='chart-table')
    
    # Run scraping function
    for i in date_urls:
        for i in playlist.find('tbody').findAll('tr'):
            song = i.find('td', class_='chart-table-track').find('strong').get_text()

            artist = i.find('td', class_='chart-table-track').find('span').get_text()
            artist = artist.replace("by ", "").strip()

            songurl = i.find('td', class_='chart-table-image').find('a').get_text('href')

            position = i.find('td', class_='chart-table-position').get_text()

            streams = i.find('td', class_='chart-table-streams').get_text()

            date = url.split("daily/")[1]

            data.append([songurl, song, artist, date, position, streams])
    
    # Stop webdriver
    browser.quit()

    # Convert to pandas DataFrame
    spotify_df = pd.DataFrame(data, columns = ["song_url", "song", "artist", "date", "position", "streams"])

    # Save as csv file in same folder
    with open('spotifytop200.csv', 'w') as x:
        spotify_df.to_csv(x, header= True, index=False)
    
    # Print dataframe
    print(spotify_df)

scrape(date_urls)











