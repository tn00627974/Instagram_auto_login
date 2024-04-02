#!/usr/bin/env python3

import argparse
import json
import customtkinter
from InstagramBot import InstagramBot

def load_accounts():
    try:
        with open("accounts.json", "r") as file:
            accounts = json.load(file)
    except FileNotFoundError:
        accounts = []
    return accounts

def save_accounts(accounts):
    with open("accounts.json", "w") as file:
        json.dump(accounts, file)

def create_bot(account):
    bot = InstagramBot()
    bot.login(email=account["username"], password=account["password"])
    return bot

def main():
    parser = argparse.ArgumentParser(description="Instagram Bot")

    parser.add_argument("-del", "--delay", type=int, default=5, help="Delay in seconds between actions")

    args = parser.parse_args()

    app = customtkinter.CTk()
    app.title("Instagram_auto_login")
    app.geometry("500x300")

    frame = customtkinter.CTkFrame(app, width=800, height=600)
    frame.pack(fill=customtkinter.BOTH, expand=True)
    
    entry_username = customtkinter.CTkEntry(frame, 
                                            placeholder_text="Username",
                                            height=40,
                                            width=400,
                                            corner_radius=15,
                                            placeholder_text_color="White",
                                            fg_color="#0074D9",
                                            font=("Arial", 20, "bold"),
                                            show='*')

    entry_password = customtkinter.CTkEntry(frame, placeholder_text="Password",
                                            height=40,
                                            width=400,
                                            corner_radius=15,
                                            placeholder_text_color="White",
                                            fg_color="#0074D9",
                                            font=("Arial", 20, "bold"),
                                            show='*')

    # textbox = customtkinter.CTkTextbox(frame, width=400, corner_radius=5, height=100)

    def add_account():
        username = entry_username.get()
        password = entry_password.get()

        # if not username or not password:
        #     textbox.insert("end", "Please enter a username and password.\n")
        #     return

        account = {
            "username": username,
            "password": password
        }

        bot = create_bot(account)
        accounts = load_accounts()
        accounts.append(account)
        save_accounts(accounts)

        # textbox.insert("end", f"Account added: {username}\n")

    def start_bot():
        accounts = load_accounts()

        if len(accounts) == 0:
            # textbox.insert("end", "No accounts found. Please add accounts first.\n")
            return

    entry_username.pack(pady=10)
    entry_password.pack(pady=10)
    button = customtkinter.CTkButton(frame, text="Start bot", command=add_account,
                                     font=("Arial", 15, "bold"))
    button.pack(pady=10)
    # textbox.pack(pady=15)
    button_start = customtkinter.CTkButton(frame, text="Start", command=start_bot,
                                           font=("Arial", 15, "bold"),
                                           corner_radius=10)
    # button_start.pack(pady=25)

    app.mainloop()
    
if __name__ == "__main__":
    main()
