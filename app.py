import observers
import logging
from win10toast import ToastNotifier


logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')


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

    def on_open():
        toast = ToastNotifier()
        toast.show_toast(
            "vaqte sefarat",
            "vaqt",
            duration = 20,
            threaded = True,
            )


    def on_fail():
        logging.info("Baz nashode hanuz :((( ")


    observers.observer_bs4_banner(
        expired_text="from 17th July",
        refresh_time_secs = 5,
        onopen= on_open,
        onfail= on_fail 
        )

