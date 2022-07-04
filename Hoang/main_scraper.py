from selenium import webdriver
from selenium.webdriver.common.by import By
import time, json, os
from scrape_season import get_season_data

driver = webdriver.Edge()
with open('leagues.json') as f:
    leagues = json.load(f)

for league in leagues.keys():
    os.makedirs(league, exist_ok= True)
    seasons = list(leagues[league].keys())[1:]
    for season in seasons:
        dir = os.path.join(league, season.replace("/","_"))
        os.makedirs(dir, exist_ok= True)

        season_url = "https://1xbet.whoscored.com"+leagues[league][season]

        get_season_data(dir, driver, season_url)
driver.quit()
