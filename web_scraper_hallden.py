from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

## get the url for the site that you want to scrape
url = 'https://www.youtube.com/kallehallden/videos'

## initiate a webdriver
driver = webdriver.Chrome()
driver.get(url)

## wait 5 seconds
wait = WebDriverWait(driver, 5)

## locate all elements with xpath
elements = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="video-title"]'))) 

print(elements['aria-label'])
driver.close()
