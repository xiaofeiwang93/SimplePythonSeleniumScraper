from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Users/xiaofeiwang/Documents/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com")

searchBox = driver.find_element_by_name('q')
searchBox.send_keys("Python Selenium Tutorial")
searchBox.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    print(main.text)

finally:
    driver.quit()
