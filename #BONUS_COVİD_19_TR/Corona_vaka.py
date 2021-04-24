from selenium import webdriver
import time
driver = webdriver.Chrome()

url = "https://covid19.saglik.gov.tr/TR-66935/genel-koronavirus-tablosu.html"
driver.get(url)
time.sleep(2)
