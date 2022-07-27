from random import choices
import winsound
import easygui
import time
import logging
from bs4 import BeautifulSoup
import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')

def observer_bs4_banner(expired_text, refresh_time_secs, onopen, onfail):
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

def play_sound(secs=None):
    x = 200
    for i in range(secs if secs is not None else 100000):
        winsound.Beep(x+400, 333)
        winsound.Beep(x+200, 333)
        winsound.Beep(x, 334)
        if i%2: x += 50
        if x >= 1000: x = 200

# def show_notiftoast():
#     toast = ToastNotifier()
#     toast.show_toast(
#         "Appoinments are opened to book now!!",
#         "Check www.ckgsir.com",
#         threaded = False,
#         )


if __name__ == '__main__':
    title="CoxBot - Banner Observer"
    
    observe_choices = ['Banner (Hidden)']

    observe_type = 'Banner (Hidden)' #easygui.buttonbox("Select the observer you need", title, choices=observe_choices)
    expired_text = easygui.enterbox("IMPORTANT!\nEnter the current date mentioned in the banner.\n(Any changes in the banner means opening new times)", title, default='from 17th July')
    if not expired_text:
        easygui.msgbox("Operation canceled!", title)
        exit()
    refresh_secs = easygui.integerbox("Enter refresh rate in seconds", title, default=20)
    if not refresh_secs:
        easygui.msgbox("Operation canceled!", title)
        exit()
    sound_alarm = easygui.integerbox("Sound alarm duration:", title, 30000, 10, 100000) or 30000

    def on_open():
        logging.info("OPEN!!!")
        play_sound(sound_alarm)
        

    def on_fail():
        logging.info("Still closed!")

    print("Observer: ", observe_type)
    print("Refresh rate (seconds): ", refresh_secs)
    if expired_text: print("Expired date: ", expired_text)
    print("Sound alarm: ", "Enabled" if sound_alarm else "Disabled")
    print("Sound alarm dureation (Seconds): ", sound_alarm)

    print("\n( Enter Ctrl+C to Stop )")
    print("============================================")

    
    
    observer_bs4_banner(
        expired_text=expired_text,
        refresh_time_secs = refresh_secs,
        onopen= on_open,
        onfail= on_fail 
        )



