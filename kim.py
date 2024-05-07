import json
import os

def get_user_input():
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

    while True:
        print("\nOptions:")
        print("1. Add user")
        print("2. Delete user")
        print("3. Exit")

        option = input("Choose an option: ")

        if option == "1":
            # Add user
            print("Enter user details:")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            phone_number = input("Phone Number: ")
            job_title = input("Desired Job Title: ")
            location = input("Preferred Location: ")
            user_id = len(all_users_data) + 1

            user_data = {
                "user_id": user_id,
                "first_name": first_name,
                "last_name": last_name,
                "phone_number": phone_number,
                "job_title": job_title,
                "location": location
            }

            all_users_data.append(user_data)

            with open('user_data.json', 'w') as file:
                json.dump(all_users_data, file, indent=4)

            print("User added successfully!")
            print(f"Your user ID is: {user_id}")

        elif option == "2":
            print("Enter user ID to delete:")
            user_id = input("User ID: ")

            all_users_data = [user for user in all_users_data if user.get('user_id') != int(user_id)]

            with open('user_data.json', 'w') as file:
                json.dump(all_users_data, file, indent=4)

            print("User deleted successfully!")

        elif option == "3":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose again.")

    return all_users_data

new_user_data = get_user_input()
print("\nUpdated user data:")
print(new_user_data)
