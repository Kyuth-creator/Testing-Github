from selenium import webdriver
from selenium.webdriver.chrome.service  import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
products = "product"
products_price = "productPrice"

driver.get("https://orteil.dashnet.org/cookieclicker/")
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)
English = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
English.click()
WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "bigCookie"))
    )
cookie = driver.find_element(By.ID, "bigCookie")
while True:
    cookie.click()
    WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'cookies'))
    )
    cookie_amount = driver.find_element(By.ID, 'cookies').text
    cookie_amount = int(cookie_amount.split("\n")[0].split()[0])

    for i in range(4):
        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, products_price + str(i)))
        )
        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, products + str(i)))
        )
        product = driver.find_element(By.ID, products_price + str(i)).text
        if not product.isdigit():
            continue
        product = int(product.replace(",", ""))
        if cookie_amount >= product:
            WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, products + str(i)))
            )
            product_click = driver.find_element(By.ID, products + str(i))
            product_click.click()
            break
            
    

