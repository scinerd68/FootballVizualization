from selenium.webdriver.common.by import By
import time,os

def scrape_table(dir, driver, table_id, postfix="",):
    scraped = ""
    table = driver.find_element(By.ID, table_id)
    headers = table.find_elements(By.TAG_NAME, "th")
    for header in headers:
        scraped += (header.text+',')
    scraped = scraped[:-1]
    scraped += '\n'

    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        for col in cols:
            scraped += (col.text+",")
        scraped = scraped[:-1]
        scraped += '\n'


    with open(os.path.join(dir,table_id+postfix+".csv"), "w") as f:
        f.write(scraped)

def get_season_data(dir, driver,season_url):

    driver.get(season_url)
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, "//*[@id=\"sub-navigation\"]/ul/li[3]/a").click();
    driver.implicitly_wait(2)
    team_table_ids = ['stage-team-stats-summary','stage-team-stats-defensive','stage-team-stats-offensive','stage-team-stats-detailed']
    situation_table_ids =['stage-goals', 'stage-passes', 'stage-cards']
    pitch_table_ids = ['stage-touch-channels', 'stage-attempt-directions', 'stage-attempt-zones', 'stage-touch-zones']

    for i in range(1,5):
        driver.find_element(By.XPATH,"//*[@id=\"stage-team-stats-options\"]/li["+str(i)+"]/a").click();
        time.sleep(2)
        scrape_table(dir, driver, team_table_ids[i-1])

    for i in range(1,3):
        driver.find_element(By.XPATH, "//*[@id=\"stage-situation-stats-options\"]/li["+str(i)+"]/a").click();
        time.sleep(2)

        driver.find_element(By.XPATH, "//*[@id =\""+situation_table_ids[i - 1]+"-filter-against\"]/dl/dd[1]/a").click();
        time.sleep(2)
        scrape_table(dir, driver, situation_table_ids[i - 1],"-for")

        driver.find_element(By.XPATH, "//*[@id =\""+situation_table_ids[i - 1]+"-filter-against\"]/dl/dd[2]/a").click();
        time.sleep(2)
        scrape_table(dir, driver, situation_table_ids[i - 1],"-against")

    driver.find_element(By.XPATH, "//*[@id=\"stage-situation-stats-options\"]/li[" + str(3) + "]/a").click();
    time.sleep(2)
    scrape_table(dir, driver, situation_table_ids[2])

    for i in [1,4]:
        driver.find_element(By.XPATH,"//*[@id=\"stage-pitch-stats-options\"]/li["+str(i)+"]/a").click();
        time.sleep(2)
        scrape_table(dir, driver, pitch_table_ids[i-1])

    for i in [2,3]:

        driver.find_element(By.XPATH,"//*[@id=\"stage-pitch-stats-options\"]/li["+str(i)+"]/a").click();
        time.sleep(2)

        driver.find_element(By.XPATH, "//*[@id=\""+ pitch_table_ids[i-1]+"-filter-against\"]/dl/dd[" + str(1) + "]/a").click();
        time.sleep(2)
        scrape_table(dir, driver, pitch_table_ids[i-1],"-for")
        driver.find_element(By.XPATH, "//*[@id=\""+pitch_table_ids[i-1]+"-filter-against\"]/dl/dd[" + str(2) + "]/a").click();
        time.sleep(2)
        scrape_table(dir, driver, pitch_table_ids[i - 1], "-against")


