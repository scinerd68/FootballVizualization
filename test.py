from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import csv

# Set the location of the webdriver
PATH = "D:\\chromedriver.exe"

# Instantiate a webdriver
driver = webdriver.Chrome(PATH)
wait = WebDriverWait(driver, 20)
driver.get("https://1xbet.whoscored.com/Regions/252/Tournaments/2/Seasons/4311/Stages/9155/TeamStatistics/England-Premier-League-2014-2015")
try:
    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Offensive")))
    link.click()
except:
    driver.quit()
# wait.until(EC.staleness_of(link))
# wait.until(EC.presence_of_element_located((By.ID, "statistics-team-table-offensive")))
time.sleep(5)
# table = driver.find_element_by_id("statistics-team-table-offensive")
# print(table.text)
soup = BeautifulSoup(driver.page_source, 'lxml')
table = soup.find(id="statistics-team-table-offensive").table
# print(table.text)
header = [title.text for title in table.thead.tr.find_all('th')]
with open('table2.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(header)

    body = table.tbody
    for row in body.find_all('tr'):
        row_data = [data.text for data in row.find_all('td')]
        row_data[0] = row_data[0][3:].strip() # remove index of each team
        writer.writerow(row_data)

driver.quit()