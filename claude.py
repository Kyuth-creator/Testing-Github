from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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
driver.find_element(By.CLASS_NAME, "fi-flight").click()

# Close notification
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "close-icon"))
)
time.sleep(1)
driver.find_element(By.CLASS_NAME, "close-icon").click()

# Fill in the Leaving field
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder,'Going')]"))
)
leaving = driver.find_element(By.XPATH, "//input[contains(@placeholder,'Going')]")
leaving.click()
leaving.send_keys("japan")
time.sleep(1.5)                   # let the dropdown suggestions load
leaving.send_keys(Keys.ARROW_DOWN)  # move into the dropdown
time.sleep(0.5)
leaving.send_keys(Keys.ENTER)       # confirm the selection
time.sleep(10)
driver.quit()
