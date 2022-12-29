from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://www.amazon.de/s?k=self+help+books&sprefix=self+hel%2Caps%2C101&ref=nb_sb_ss_ts-doa-p_1_8'

# initiate a webdriver
driver = webdriver.Chrome()
driver.get(url)

#wait 5 seconds
wait = WebDriverWait(driver, 5)

#locate all elements with xpath
elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")))

#get the text attribute and print them
for element in elements:
    print(element.text)

    print('------')

#close the driver
driver.close()