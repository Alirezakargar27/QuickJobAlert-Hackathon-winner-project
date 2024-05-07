import requests
import json

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

    try:
        response_data = response.json()
    except ValueError:
        print("Error: Unable to parse JSON response.")
        

    if response.status_code == 200:
        print("SMS sent successfully! Response:", response_data)
    else:
        print(f"Error: Failed to send SMS. Status Code: {response.status_code}, Details: {response_data}")
#uncomment when not needed
send_sms_with_requests("+1234", "Hallo test")
