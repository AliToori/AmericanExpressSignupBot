#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver import ActionChains
import pyautogui


# **********************************************************************
# This method is for site login
# **********************************************************************
def site_login(url, first_name, last_name, email, card_number):
    driver.get(url)
    try:
        btn_login = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div[1]/section[3]/div[2]/a[1]')))
        btn_login.click()
    except TimeoutException as tex:
        print("EXCEPTION IN SIGNOUT:", tex.msg)
        time.sleep(3)
        element = driver.find_element_by_class_name('iNavLinkLabel').click()
        actions = ActionChains(driver)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()
        time.sleep(3)

        btn_login = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div[1]/section[3]/div[2]/a[1]')))
        btn_login.click()
    form = driver.find_element_by_id('enrolment-form')
    fname = form.find_element_by_id('firstName')
    fname.clear()
    fname.send_keys(' ')
    fname.send_keys(first_name)
    lname = form.find_element_by_id('lastName')
    lname.clear()
    lname.send_keys(' ')
    lname.send_keys(last_name)
    cnumber = form.find_element_by_id('cardNumber')
    cnumber.clear()
    cnumber.send_keys(' ')
    cnumber.send_keys(card_number)
    email_f = form.find_element_by_id('email')
    email_f.clear()
    email_f.send_keys(' ')
    email_f.send_keys(email)
    time.sleep(1)
    # Click Button: Confirm
    btn = form.find_element_by_xpath('//*[@id="submitButton"]')
    driver.execute_script('arguments[0].scrollIntoView(true);', btn)
    time.sleep(1)
    btn.click()
    time.sleep(3)
    try:
        # Click link text: click here
        driver.find_element_by_class_name('signout-btn').click()
        print("Clicked: Sign-out")
        time.sleep(3)
    except WebDriverException as e:
        print(e.msg)
        try:
            driver.find_element_by_xpath('//*[@id="enrolment-form"]/div[2]/div/div[2]/p[2]/a').click()
            print("Clicked: Click here")
            time.sleep(3)
        except WebDriverException as ex:
            print(ex.msg)
            # Click Button: Close
            driver.find_element_by_xpath('//*[@id="enrolment-form"]/p[2]/input').click()
            print("Clicked: Close")
            time.sleep(3)
    # Click Button: Sign-out
    # element = driver.find_element_by_class_name('iNavLinkLabel')
    pyautogui.moveTo(x=1000, y=180)
    time.sleep(1)
    pyautogui.click(x=1000, y=180, button='left')
    time.sleep(3)


# **********************************************************************
#    The program starts from here
# **********************************************************************
# Please install the selenium and download chromewebdriver.exe before running the script
# Put all of your web-urls here in this list separated by commas
web_urls = [
    "https://www.americanexpress.com/au/network/shopping/doe-offer-detail.html?offer=5438",
    "https://www.americanexpress.com/au/network/shopping/doe-offer-detail.html?offer=86383"
            ]

first_name = "Zhi Yuan"
last_name = "Chua"
card_numbers = ["377348147621005", "377348102631007"]
email = "dfgdfg@hotmail.com"
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome('/Users/s87262/Desktop/chromedriver', options=options)
# driver = webdriver.Chrome(options=options)
for card_number in card_numbers:
    for url in web_urls:
        site_login(url=url, first_name=first_name, last_name=last_name, card_number=card_number, email=email)



driver.close()