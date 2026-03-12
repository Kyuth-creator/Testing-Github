from selenium import webdriver
from selenium.webdriver.chrome.service  import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

#service = Service(executable_path="chromedriver.exe")
#driver = webdriver.Chrome(service=service)

#user info ------------------------------------
Departure = input("Where are you departing from?(city): ").strip()
Destination = input("Where are you going?(city): ").strip()
Departure_month = input("Which months are you planning to leave?: ").strip()
Destination_month = input("Which months are you planning to return?: ").strip()

#used chrome-manager cuz i keep losing chromedriver.exe
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


wait = WebDriverWait(driver, 10)
driver.get("https://www.trip.com/")

wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "fi-flight"))
)
Flight = driver.find_element(By.CLASS_NAME, "fi-flight")
Flight.click()
# i should add an option of one way multiway or whatever. using [] or sth like asking 1 2 3 for the options not now tho

# closing the notification
wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "close-icon"))
)
close_icon = driver.find_element(By.CLASS_NAME, "close-icon")
time.sleep(1)
close_icon.click()

#clicking the calendar
wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder,'Any date')]"))
)
calendar = driver.find_element(By.XPATH, "//input[contains(@placeholder,'Any date')]")
calendar.click()

#logic for finding month -----------------------------
while True:

    wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "c-fuzzy-calendar-month__title"))
    )
    month = driver.find_elements(By.CLASS_NAME, "c-fuzzy-calendar-month__title")

    current_month = month[0].text
    current_month_used = current_month.split()[0]

    months = [
        "January",    # 1
        "February",   # 2
        "March",      # 3
        "April",      # 4
        "May",        # 5
        "June",       # 6
        "July",       # 7
        "August",     # 8
        "September",  # 9
        "October",    # 10
        "November",   # 11
        "December"    # 12
    ]

    current_month_used_value = months.index(current_month_used.capitalize()) # i need to constantly update the current month
    Departure_month_value = months.index(Departure_month.capitalize())
    Destination_month_value = months.index(Destination_month.capitalize())

    if current_month_used_value == Departure_month_value:

        wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "day"))
        )
        date = driver.find_element(By.XPATH, f"//*[@data-date='2026-0{Departure_month_value+1}-17']")
        date.click()
        while True:
            # i need to constantly updates the current to continue checking
            wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "c-fuzzy-calendar-month__title"))
            )
            month = driver.find_elements(By.CLASS_NAME, "c-fuzzy-calendar-month__title")
            current_month_2 = month[0].text
            current_month_used_2 = current_month_2.split()[0]
            current_month_used_value_2 = months.index(current_month_used_2.capitalize())
            if current_month_used_value_2 == Destination_month_value:
                # i need to change the active section for dates
                wait.until(
                    EC.presence_of_element_located((By.CLASS_NAME, "nh_d-arrive"))
                )
                return_section = driver.find_element(By.CLASS_NAME, "nh_d-arrive")
                return_section.click()
                wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "day"))
                )
                date = driver.find_element(By.XPATH, f"//*[@data-date='2026-0{Destination_month_value+1}-17']")
                date.click()
                time.sleep(10) #-======================
                break
            elif current_month_used_value + 1 <= Destination_month_value:
                wait.until(
                    EC.presence_of_element_located((By.CLASS_NAME, "c-fuzzy-calendar-icon-next"))
                )
                next_icon = driver.find_element(By.CLASS_NAME, "c-fuzzy-calendar-icon-next")
                next_icon.click()
            else:
                break
        break
            
    elif current_month_used_value + 1 <= Departure_month_value:
        wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "c-fuzzy-calendar-icon-next"))
        )
        next_icon = driver.find_element(By.CLASS_NAME, "c-fuzzy-calendar-icon-next")
        next_icon.click()
    else:
        break

time.sleep(5)
driver.quit()