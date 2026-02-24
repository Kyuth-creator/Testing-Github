from selenium import webdriver
from selenium.webdriver.chrome.service  import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.trip.com/")

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "fi-flight"))
)
Flight = driver.find_element(By.CLASS_NAME, "fi-flight")
Flight.click()
# i should add an option of one way multiway or whatever. using [] or sth like asking 1 2 3 for the options not now tho
# closing the notification
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "close-icon"))
)
close_icon = driver.find_element(By.CLASS_NAME, "close-icon")
time.sleep(1)
close_icon.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "module-input"))
)
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "fuzzy-input"))
)

leaving = driver.find_element(By.CLASS_NAME, "module-input")
leaving.clear()
leaving.click(
)
leaving.send_keys("japan")
leaving.send_keys(Keys.ENTER)




time.sleep(10)

driver.quit()









