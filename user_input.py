import json
import os
from colorama import Fore, Style
import send_sms


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

    return all_users_data

def read_user_data(path="user_data.json"):
    with open(path, "r") as fObj:
        data = json.load(fObj)
    return data


def show_menue():
    """show menue"""
    while True:
        print(f"\n{Fore.CYAN}Welcome to QuickJobAlerts{Style.RESET_ALL}")
        print(f"{Fore.RED}We save your time!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Are you tired of missing out on job opportunities?{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}make a profile and we'll keep you informed every 24 hours{Style.RESET_ALL}")
        print(f"\n{Fore.GREEN}Options:{Style.RESET_ALL}")
        print("1. Make Profile")
        print("2. Delete Profile")
        print("3. Exit")

        print(f"{Fore.GREEN} Real time SMS Status of Users: {Style.RESET_ALL}")
        all_users_data = read_user_data()
        option = input(f"{Fore.GREEN}Choose an option: {Style.RESET_ALL}")

        if option == "1":
            print(f"\n{Fore.GREEN}Please enter your personal data:{Style.RESET_ALL}")
            first_name = input("Enter your first name: ")
            last_name = input("Enter your Last name: ")
            phone_number = input("Enter your phone number (with country code, e.g. +1234567890): ")
            job_title = input("What is your desired Job Title: ")
            location = input("What is your preferred Location(e.g Germany): ")
            user_id = len(all_users_data) + 1

            user_data = {
                'user_id': user_id,
                'first_name': first_name,
                'last_name': last_name,
                'phone_number': phone_number,
                'job_title': job_title,
                'location': location
            }

            all_users_data.append(user_data)

            with open('user_data.json', 'w') as file:
                json.dump(all_users_data, file, indent=4)

            print(f"\n{Fore.GREEN}User added successfully!{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Your user ID is: {user_id}{Style.RESET_ALL}")

            send_sms.send_sms_to_user(False)

        elif option == "2":
            user_id = input("Please enter your user ID: ")

            all_users_data = [user for user in all_users_data if user.get('user_id') != int(user_id)]

            with open('user_data.json', 'w') as file:
                json.dump(all_users_data, file, indent=4)

            print(f"\n{Fore.GREEN}Your profile deleted! We wish you success in your Career{Style.RESET_ALL}")

        elif option == "3":
            print("bye bye!")
            break

        else:
            print("\n{Fore.RED}Invalid option. Please choose again.{Style.RESET_ALL}")

    return all_users_data


#if __name__ == "__main__":
   # new_user_data = get_user_input()
    #print("\nUpdated user data:")
   # print(new_user_data)
