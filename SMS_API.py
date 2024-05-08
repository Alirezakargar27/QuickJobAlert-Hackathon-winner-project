import requests
import json


def send_sms_with_requests(phone_number, message):
    """Implementing SMS API """
    try:
        # API endpoint
        url = "https://xlzm4g.api.infobip.com/sms/2/text/advanced"

        # Headers for authorization and content type
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

        # Send POST request to the API endpoint
        response = requests.post(url, json=payload, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            print("SMS sent successfully!")
        else:
            print(f"Failed to send SMS. Status Code: {response.status_code}, Details: {response.text}")
    except Exception as e:
        print(f"An error occurred while sending the SMS: {e}")


# Test the function
send_sms_with_requests("+1234567890", "Hello, this is a test message from QuickJobAlerts!")
