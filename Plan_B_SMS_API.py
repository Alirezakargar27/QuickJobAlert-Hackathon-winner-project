# this is the plan B API for sending SMS considering the limitation with initial API it shall not be used in the main file yet
from sinch import SinchClient

def send_sms_with_sinch(phone_number, message):
    sinch_client = SinchClient(
        key_id="fe6cc05f-d883-4955-b926-65c203dde5ef",
        key_secret="5ovoJMtVl6k_aafZ4-uIZnjJgx",
        project_id="24882eee-2025-4616-a45e-2cf9a4313d6e"
    )

    send_batch_response = sinch_client.sms.batches.send(
        body=message,
        to=[phone_number],
        from_="+447520650936",
        delivery_report="none"
    )

    print(send_batch_response)
