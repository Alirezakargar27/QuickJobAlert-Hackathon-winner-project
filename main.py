
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

