from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = r'C:\Program Files\chrome webdriver\chromedriver-win64\chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]').click()


dropdown = Select(driver.find_element(By.ID, 'country'))
dropdown.select_by_visible_text('Spain')

time.sleep(3)

matches = driver.find_elements(By.TAG_NAME, 'tr')

# //tr/td[1]
date = []
home_team = []
score = []
away_team = []

for match in matches:
    tds = match.find_elements(By.TAG_NAME, 'td')
    if len(tds) >= 5:
        date.append(match.find_element(By.XPATH, './/td[1]').text)
        home = match.find_element(By.XPATH, './/td[3]').text
        home_team.append(home)
        print(home)
        score.append(match.find_element(By.XPATH, './/td[4]').text)
        away_team.append(match.find_element(By.XPATH, './/td[5]').text)


df = pd.DataFrame({
    'date': date,
    'home_team': home_team,
    'score': score,
    'away_team': away_team
})
df.to_csv('matches_data.csv', index=False)
print(df)




input("Press Enter to close")
# driver.quit()



