import json
from ali import fetch_job_listing

def main():
    api_key = "471cdc11-45b6-419c-8c52-2c1a99f3d072"

    with open('user_data.json', 'r') as file:
        all_users_data = json.load(file)

    for user_data in all_users_data:
        print(f"Fetching job listing for {user_data.get('first_name')} {user_data.get('last_name')}:")
        job_listing = fetch_job_listing(api_key, user_data)
        if job_listing:
            print(job_listing)
        else:
            print("No job listing found.")

if __name__ == "__main__":
    main()
