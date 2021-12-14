from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = r"C:\Programowanie\Python\skate_scraper\chromedriver.exe"
TAX_OFFICE_WEB = "https://ventus.enalog.se/Booking/Booking/Index/SUA"

browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
browser.get(TAX_OFFICE_WEB)