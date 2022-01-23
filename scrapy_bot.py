from selenium import webdriver
from time import sleep

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