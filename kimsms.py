import requests
import json

<<<<<<< HEAD
def send_sms_with_requests(phone_number, message):
    # Api info & endpoint
    url = "https://xlzm4g.api.infobip.com/sms/2/text/advanced"
    
    #authorization key
    headers = {
        'Authorization': 'App ba0f53e2c0de6421ad8433544c855b72-acb9e624-7378-4d67-bda6-d560b9403cb8',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    # Payload with the SMS message and destination
    payload = {
        "messages": [
            {
                "destinations": [{"to": phone_number}],
                "from": "QuickJobAlerts",  
                "text": message
            }
        ]
    }

    response = requests.post(url, json=payload, headers=headers)
=======
BASE_URL = "https://xlzm4g.api.infobip.com"
SEND_SMS_URL = "/sms/2/text/advanced"
>>>>>>> 021b529e1464a625f94a9e9b58560cdf9ce3844d

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

<<<<<<< HEAD
    if response.status_code == 200:
        print("SMS sent successfully! Response:", response_data)
    else:
        print(f"Error: Failed to send SMS. Status Code: {response.status_code}, Details: {response_data}")
#uncomment when not needed
=======
>>>>>>> 021b529e1464a625f94a9e9b58560cdf9ce3844d
