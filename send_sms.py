import json
from datetime import datetime, timedelta
import time
from Job_API import fetch_job_listing
from SMS_API import send_sms_with_requests
import generate_html
import user_input
def send_sms_to_user(do_sleep):

    api_key = "471cdc11-45b6-419c-8c52-2c1a99f3d072"

    #get all user data
    all_user_data = user_input.get_user_input()
    print("Checking for new job listings...")

    # iterate over each user
    for user_data in all_user_data:
        print(f"Fetching job listing for {user_data.get('first_name')} {user_data.get('last_name')}")

        # fetch the latest job listing for the user
        job_listing = fetch_job_listing(api_key, user_data)

        # Check if a new job listing was found
        if job_listing:
            job_id = job_listing.get("id")
            job_link = job_listing.get("link")
            phone_number = user_data.get("phone_number")
            user_name = user_data.get("first_name")

            # Check for repetetive job id
            if "jobs" not in user_data or not any(job.get("id") == job_id for job in user_data["jobs"]):
                # Send SMS
                message = f"Hi {user_name}, we found a new job for you! {job_link} - QuickJobAlerts"
                send_sms_with_requests(phone_number, message)
            else:
                print("Job already exists in user's database. Skipping SMS notification.")

        generate_html.generate_website()

    # Wait for 24 hours before checking again
    print("Waiting for next check in 24 hours...")
    if do_sleep == True:
        time.sleep(86400)

