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
    sound_alarm = easygui.integerbox("Do you want to play sound alarm?\nSo enter the duration in seconds.\nOtherwise tap 'Cancel'", title, 30000, 10, 100000)

    def on_open():
        
        if sound_alarm:
            alarm_thread = threading.Thread(target=play_sound, args=(sound_alarm,))
            alarm_thread.start()

        show_notiftoast()
        

    def on_fail():
        logging.info("Still closed!")

    print("Observer: ", observe_type)
    print("Refresh rate (seconds): ", refresh_secs)
    if expired_text: print("Expired date: ", expired_text)
    print("Sound alarm: ", "Enabled" if sound_alarm else "Disabled")
    print("Sound alarm dureation (Seconds): ", sound_alarm)

    print("\n( Enter Ctrl+C to Stop )")
    print("============================================")

    
    # if observe_type == 'Banner (Selenium)':    
    #     observers.observer_selenium_banner(
    #         expired_text=expired_text,
    #         refresh_time_secs = refresh_secs,
    #         onopen= on_open,
    #         onfail= on_fail 
    #         )
    
    observers.observer_bs4_banner(
        expired_text=expired_text,
        refresh_time_secs = refresh_secs,
        onopen= on_open,
        onfail= on_fail 
        )
    # elif observe_choices == 'Appoinment calender':
    #     easygui.msgbox("Not yet implemented!", title)        
    #     exit()
    # else:
    #     easygui.msgbox("Operation canceled!", title)
    #     exit()



