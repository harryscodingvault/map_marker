from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("E:\Portfolio_Proj\Python\mapping\chromedriver")
sleep(0.5)

driver.get("https://www.linkedin.com")
sleep(5)

driver.find_element_by_link_text("Sign in").click()
sleep(3)

# LOGIN PAGE
import os

username_input =  driver.find_element_by_name("session_key")
username_input.send_keys( os.getenv('EMAIL_LINKEDIN'))
sleep(0.5)

password_input =  driver.find_element_by_name("session_password")
password_input.send_keys(os.getenv('PASS_LINKEDIN'))
sleep(0.5)

driver.find_element_by_xpath('//button[text()="Sign in"]').click()
sleep(5)

driver.get("https://www.google.com")
sleep(5)

# SEARCH GOOGLE
search_input =  driver.find_element_by_name("q")
search_input.send_keys('site:linkedin.com/in/ AND "python" AND "Phoenix"')
sleep(1)

search_input.send_keys(Keys.RETURN)
sleep(3)

# GET PROFILES
profiles = driver.find_elements(By.XPATH,"//*[@class='yuRUbf']/a[1]")
profiles = [profile.get_attribute('href') for profile in profiles]
sleep(3)
