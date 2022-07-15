from random import choices
import observers
import logging
from win10toast import ToastNotifier
import winsound
import easygui
import threading


logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')


def play_sound(secs=None):
    x = 200
    for i in range(secs if secs is not None else 100000):
        winsound.Beep(x+400, 333)
        winsound.Beep(x+200, 333)
        winsound.Beep(x, 334)
        if i%2: x += 50
        if x >= 1000: x = 200

def show_notiftoast():
    toast = ToastNotifier()
    toast.show_toast(
        "Appoinments are opened to book now!!",
        "Check www.ckgsir.com",
        threaded = False,
        )



# def send_sms(text, receivers: list):
        
#     try:
#         apikey = '344D6A4B4E546E3779566964492B4162535558776A48392F4C5455363372546A6E555A4A5861595747626B3D'
#         api = kavenegar.KavenegarAPI(apikey)
#         params = {
#             'receptor': ','.join(receivers),
#             'message': 'Kaveh specialized Web service '
#         }   
    
#         response = api.sms_send(params)
#         logging.info("SMS response: "+response)
#     except kavenegar.APIException as e: 
#         logging.error(e)
#     except kavenegar.HTTPException as e: 
#         logging.error(e)        

if __name__ == '__main__':
    title="CoxBot: Config"
    
    observe_choices = ['Banner (Hidden)', 'Banner (Selenium)', 'Appoinment calender']

    observe_type = easygui.buttonbox("Select the observer you need", title, choices=observe_choices)
    if observe_type in ['Banner (Selenium)', 'Banner (Hidden)']:
        expired_text = easygui.enterbox("IMPORTANT!\nEnter the current date mentioned in the banner.\n(Any changes in the banner means opening new times)", title, default='from 17th July')
        if not expired_text:
            easygui.msgbox("Operation canceled!", title)
            exit()
    sound_alarm = easygui.integerbox("Do you want to play sound alarm?\nSo enter the duration in seconds.\nOtherwise tap 'Cancel'", title, default=60)

    def on_open():
        
        if sound_alarm:
            alarm_thread = threading.Thread(target=play_sound, args=(sound_alarm,))
            alarm_thread.start()

        show_notiftoast()
        

    def on_fail():
        logging.info("Still closed!")

    
    if observe_type == 'Banner (Selenium)':    
        observers.observer_selenium_banner(
            expired_text=expired_text,
            refresh_time_secs = 5,
            onopen= on_open,
            onfail= on_fail 
            )
    elif observe_type == 'Banner (Hidden)':
        observers.observer_bs4_banner(
            expired_text=expired_text,
            refresh_time_secs = 5,
            onopen= on_open,
            onfail= on_fail 
            )
    elif observe_choices == 'Appoinment calender':
        easygui.msgbox("Not yet implemented!", title)        
        exit()
    else:
        easygui.msgbox("Operation canceled!", title)
        exit()



