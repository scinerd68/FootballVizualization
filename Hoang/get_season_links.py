from selenium import webdriver
from selenium.webdriver.common.by import By
import time, json

leagues = {"EPL": {"url": 'https://1xbet.whoscored.com/Regions/252/Tournaments/2/England-Premier-League'},
            "SerieA":{"url":'https://1xbet.whoscored.com/Regions/108/Tournaments/5/Italy-Serie-A'},
            "LaLiga":{"url":'https://1xbet.whoscored.com/Regions/206/Tournaments/4/Spain-LaLiga'},
            "Bundesliga":{"url":'https://1xbet.whoscored.com/Regions/81/Tournaments/3/Germany-Bundesliga'},
            "Ligue1":{"url":'https://1xbet.whoscored.com/Regions/74/Tournaments/22/France-Ligue-1'}
           }

driver = webdriver.Edge()
for league in leagues.keys():

    driver.get(leagues[league]['url'])
    driver.implicitly_wait(2)

    driver.find_element(By.XPATH,'//*[@id="sub-navigation"]/ul/li[3]/a').click()
    driver.implicitly_wait(2)
    seasons = driver.find_element(By.ID, 'seasons')
    season_lists = seasons.find_elements(By.TAG_NAME, "option")
    for season in season_lists:
        leagues[league][season.text] = season.get_attribute('value')

    time.sleep(2)

driver.quit()
with open("leagues.json","w") as f:
    json.dump(leagues, f, indent=4)