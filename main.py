import json
from datetime import datetime, timedelta
import time
from Job_API import fetch_job_listing
from SMS_API import send_sms_with_requests
import generate_html
import user_input
import threading
import send_sms

def main():

    api_key = "471cdc11-45b6-419c-8c52-2c1a99f3d072"

    while True:
        send_sms.send_sms_to_user(True)

if __name__ == "__main__":
    t1 = threading.Thread(target=main)
    t2 = threading.Thread(target=user_input.show_menue)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

