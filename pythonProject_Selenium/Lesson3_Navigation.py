import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://rozetka.com.ua')
print("Page opened Online")
time.sleep(5)
#Navigation Commands
#1. Go back to previous 'apress' pag
driver.back()
time.sleep(5)
print("Moved to first page")
#2. Go to current page
driver.forward()
time.sleep(3)
print("Moved to second page")
#3. Page refresh command
driver.refresh()
time.sleep(5)
print("Page is Refreshed")
driver.quit()