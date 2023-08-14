import time
#Import Selenium Library
from selenium import webdriver

#Open Mozilla Firefox
driver = webdriver.Firefox()

#Open webpage
driver.get('https://google.com/')
print("Page opened Online")
time.sleep(3)
#Current URL
url = driver.current_url
print("URL_page:", url)

#Receive title page
title_cur = driver.title
print('Current title_Web-page:', title_cur)
assert title_cur == "Google", "Error. Opening page has the wrong title"

#Equal current URL with the opening URL
assert url == "https://www.google.com/", "Error.The current uRL and opening URL not equal."

#print('driver.page_source ', driver.page_source)

#The quit() function closes all the open windows.
#driver.quit()

#Close function
driver.close()
print("Browser Window closed")