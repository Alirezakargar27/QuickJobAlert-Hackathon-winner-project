import requests
import json

BASE_URL = "https://xlzm4g.api.infobip.com"
SEND_SMS_URL = "/sms/2/text/advanced"

def send_sms_message(number, msg):
    try:
        assert len(str(number)) > 5, "Destination phone number must be at least 6 digits long"
        assert msg != "", "Message text cannot be empty"

        url = BASE_URL + SEND_SMS_URL

        request_headers = {
            'Authorization': f'App ba0f53e2c0de6421ad8433544c855b72-acb9e624-7378-4d67-bda6-d560b9403cb8',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        payload = json.dumps({
            'messages': [
                {
                    'destinations': [{'to': str(number)}],
                    'from': 'QuickJobAlerts',
                    'text': str(msg)
                }
            ]
        })

        response = requests.post(url, data=payload, headers=request_headers)

        print(response.text)

    except Exception as e:
        print(f'An error occurred while attempting to send an SMS message to "{number}" (message: "{msg}").\nError: ', e)

send_sms_message("+491234", "Hello, this is a test message from QuickJobAlerts!")

