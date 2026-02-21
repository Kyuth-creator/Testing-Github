from selenium import webdriver
from selenium.webdriver.chrome.service  import Service

service = Service(executable_path="")
drive = webdriver.Chrome(service=service)