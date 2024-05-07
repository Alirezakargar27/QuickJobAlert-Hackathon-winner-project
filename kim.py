import json
import os

def get_user_input():
     # Ask the user for personal information and job preferences
    print("Enter your personal information and job search preferences:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    phone_number = input("Phone Number: ")
    job_title = input("Desired Job Title: ")
    location = input("Preferred Location: ")

     # Create a dictionary and saves the data
    user_data = {
        'first_name': first_name,
        'last_name': last_name,
        'phone_number': phone_number,
        'job_title': job_title,
        'location': location
    }

    # Load existing data if the file exists and is a valid JSON file
    if os.path.exists('user_data.json'):
        with open('user_data.json', 'r') as file:
            try:
                all_users_data = json.load(file)
                if not isinstance(all_users_data, list):
                    all_users_data = []
            except json.JSONDecodeError:
                all_users_data = []
    else:
        all_users_data = []

    # Append the new user data
    all_users_data.append(user_data)

    # Save the updated 
    with open('user_data.json', 'w') as file:
        json.dump(all_users_data, file, indent=4)

    return user_data

# Example usage
new_user_data = get_user_input()
print("\nNew user data added:")
print(new_user_data)
