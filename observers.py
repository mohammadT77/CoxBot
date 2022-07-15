import time
import os
import logging
from selenium.webdriver.common.by import By
from selenium import webdriver

SELENIUM_DRIVERS = os.listdir('drivers')

def observer_selenium_banner(expired_text, refresh_time_secs, onopen, onfail):

    def get_driver():
        try:
            return webdriver.Chrome('drivers/'+SELENIUM_DRIVERS[-1])
        except Exception as e:
            SELENIUM_DRIVERS.pop()
            return get_driver()

    driver = get_driver()
    driver.get("https://www.ckgsir.com/")

    while True:
        target = driver.find_element(By.CLASS_NAME, "marq")
        if expired_text not in target.text:
            onopen()
            break
        else:
            onfail()
            
        time.sleep(refresh_time_secs) 
        driver.refresh()
    driver.quit()


def observer_bs4_banner(target_text, refresh_time_secs, onopen, onfail):
    while True:
        target = driver.find_element(By.CLASS_NAME, "marq")
        if target_text in target.text:
            onopen()
            break
        else:
            onfail()
            
        time.sleep(refresh_time_secs) 
        driver.refresh()
    driver.quit()


