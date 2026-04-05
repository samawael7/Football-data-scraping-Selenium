from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = r'C:\Program Files\chrome webdriver\chromedriver-win64\chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]').click()
input("Press Enter to close")
driver.quit()
