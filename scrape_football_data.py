from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import time


def scrape_table(table: BeautifulSoup, output_file_name: str):
    assert output_file_name[-4:] == '.csv', 'output file must be a csv file' 

    header = [title.text for title in table.thead.tr.find_all('th')]
    with open(output_file_name, 'w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(header)

        body = table.tbody
        for row in body.find_all('tr'):
            row_data = [data.text for data in row.find_all('td')]
            # row_data[0] = row_data[0][3:].strip() # remove index of each team
            writer.writerow(row_data)


if __name__ == "__main__":
    # Set the location of the webdriver
    PATH = "/home/viet/OneDrive/Studying Materials/Introduction to Data Science/EDA Project/chromedriver_linux64/chromedriver"
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Instantiate a webdriver
    driver = webdriver.Chrome(PATH, options=chrome_options)
    wait = WebDriverWait(driver, 20)

    # Load the HTML page
    URL = "https://1xbet.whoscored.com/Regions/252/Tournaments/2/Seasons/1849/Stages/3115/TeamStatistics/England-Premier-League-2009-2010"
    driver.get(URL)

    # Scrape summary stats
    soup = BeautifulSoup(driver.page_source, 'lxml')
    table = soup.find(id="statistics-team-table-summary").table
    try:
        scrape_table(table, 'data/premier_league/2009_2010/summary.csv')
    except AssertionError:
        driver.quit()

    # Scrape goals stats
    table = soup.find(id="stage-goals").table
    try:
        scrape_table(table, 'data/premier_league/2009_2010/goals.csv')
    except AssertionError:
        driver.quit()

    # Scrape attack sides stats
    table = soup.find(id="stage-touch-channels").table
    try:
        scrape_table(table, 'data/premier_league/2009_2010/attack-sides.csv')
    except AssertionError:
        driver.quit()

    # Scrape offensive stats
    try:
        link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Offensive")))
        link.click()
    except:
        driver.quit()

    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    table = soup.find(id="statistics-team-table-offensive").table
    try:
        scrape_table(table, 'data/premier_league/2009_2010/offensive.csv')
    except AssertionError:
        driver.quit()

    # Scrape defensive stats
    try:
        link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Defensive")))
        link.click()
    except:
        driver.quit()

    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    table = soup.find(id="statistics-team-table-defensive").table
    try:
        scrape_table(table, 'data/premier_league/2009_2010/defensive.csv')
    except AssertionError:
        driver.quit()

    # Scrape detailed stats
    try:
        link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Detailed")))
        link.click()
    except:
        driver.quit()

    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    table = soup.find(id="statistics-team-table-detailed").table
    try:
        scrape_table(table, 'data/premier_league/2009_2010/detailed.csv')
    except AssertionError:
        driver.quit()

    # Scrape passes stats
    try:
        link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Pass Types")))
        link.click()
    except:
        driver.quit()

    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    table = soup.find(id="stage-passes").table
    try:
        scrape_table(table, 'data/premier_league/2009_2010/passes.csv')
    except AssertionError:
        driver.quit()

    # Scrape shot directions stats
    try:
        link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Shot Directions")))
        link.click()
    except:
        driver.quit()

    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    table = soup.find(id="stage-attempt-directions").table
    try:
        scrape_table(table, 'data/premier_league/2009_2010/shot-directions.csv')
    except AssertionError:
        driver.quit()

    # Scrape shot zones stats
    try:
        link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Shot Zones")))
        link.click()
    except:
        driver.quit()

    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    table = soup.find(id="stage-attempt-zones").table
    try:
        scrape_table(table, 'data/premier_league/2009_2010/shot-zones.csv')
    except AssertionError:
        driver.quit()

    # Scrape action zones stats
    try:
        link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Action Zones")))
        link.click()
    except:
        driver.quit()

    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    table = soup.find(id="stage-touch-zones").table
    try:
        scrape_table(table, 'data/premier_league/2009_2010/action-zones.csv')
    except AssertionError:
        driver.quit()

    driver.quit()