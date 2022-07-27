from pydoc import classname
import time
import os
import logging
from selenium.webdriver.common.by import By
from selenium import webdriver

# SELENIUM_DRIVERS = os.listdir('drivers')

# def observer_selenium_banner(expired_text, refresh_time_secs, onopen, onfail):

#     def get_driver():
#         try:
#             return webdriver.Chrome('drivers/'+SELENIUM_DRIVERS[-1])
#         except Exception as e:
#             SELENIUM_DRIVERS.pop()
#             return get_driver()

#     driver = get_driver()
#     driver.get("https://www.ckgsir.com/")

#     while True:
#         target = driver.find_element(By.CLASS_NAME, "marq")
#         if expired_text not in target.text:
#             onopen()
#             break
#         else:
#             onfail()
            
#         time.sleep(refresh_time_secs) 
#         driver.refresh()
#     driver.quit()


def observer_bs4_banner(expired_text, refresh_time_secs, onopen, onfail):
    from bs4 import BeautifulSoup
    import requests
    
    
    while True:
        try:
            page = requests.get("https://www.ckgsir.com")
    
            soup = BeautifulSoup(page.text, 'html.parser')
            elem = soup.find_all("div", {"class": "marq"})[0]
            spanElem = elem.find('span')
            span_text = spanElem.text
        
            if expired_text not in span_text:
                onopen()
                break
            else:
                onfail()
            
        except Exception as e:
            logging.error(e)
            continue
        finally:
            time.sleep(refresh_time_secs) 
            
        