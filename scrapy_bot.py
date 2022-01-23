from selenium import webdriver
from time import sleep
from parsel import Selector
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

import parameters

writer = csv.writer(open(parameters.RESULT_FILE, 'w'))
writer.writerow(['name', 'url'])

driver = webdriver.Chrome("E:\Portfolio_Proj\Python\mapping\chromedriver")
sleep(0.5)

driver.get("https://www.linkedin.com")
sleep(5)

driver.find_element_by_link_text("Sign in").click()
sleep(3)

# LOGIN PAGE
import os

username_input =  driver.find_element_by_name("session_key")
username_input.send_keys( parameters.EMAIL_LINKEDIN)
sleep(0.5)

password_input =  driver.find_element_by_name("session_password")
password_input.send_keys(parameters.PASS_LINKEDIN)
sleep(0.5)

driver.find_element_by_xpath('//button[text()="Sign in"]').click()
sleep(15)

# SEARCH GOOGLE
driver.get("https://www.google.com")
sleep(5)

search_input =  driver.find_element_by_name("q")
search_input.send_keys(parameters.SEARCH_QUERY)
sleep(1)

search_input.send_keys(Keys.RETURN)
sleep(3)

# GET PROFILES
profiles = driver.find_elements(By.XPATH,"//*[@class='yuRUbf']/a[1]")
profiles = [profile.get_attribute('href') for profile in profiles]
for profile in profiles:
    driver.get(profile)
    sleep(5)

    sel = Selector(text=driver.page_source)

    name = sel.xpath("//title/text()").extract_first().split("|")[0]
    p_url = driver.current_url

    print('\n')
    print(name)
    print(p_url)

    writer.writerow([name, p_url])

    try: 
        driver.find_element(By.XPATH, '//*[text()="More..."]').click()
        sleep(1)

        driver.find_element(By.XPATH, '//*[text()="Connect"]').click()
        sleep(1)

        driver.find_element(By.XPATH, '//*[text()="Send now"]').click()
        sleep(1)

    except:
        pass

driver.quit()
