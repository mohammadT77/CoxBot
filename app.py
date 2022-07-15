
import time
from win10toast import ToastNotifier
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.
toast = ToastNotifier()
driver.get("https://www.ckgsir.com/")

while True:
    target = driver.find_element(By.CLASS_NAME, "marq")
    if "from 31th July" in target.text:
        
        toast.show_toast(
            "vaqte sefarat",
            "vaqt",
            duration = 20,
            threaded = True,
        )

        break
    else:
        toast.show_toast(
            "baz nashode hanooz",
            "vaqt",
            duration = 20,
            threaded = True,
        )
        print(str(datetime.datetime.now())+ " : Baz nashode hanuz :(")
    time.sleep(5) 
    driver.refresh()


driver.quit()