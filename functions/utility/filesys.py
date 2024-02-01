import os
import sys
import json

files_path = os.path.dirname(os.path.abspath(sys.argv[0]))
User_folder = os.path.join(files_path, "User")
if not os.path.exists(User_folder):
    os.makedirs(User_folder)

text_files_folder = os.path.join(User_folder, "Accounts")
text_file = os.path.join(text_files_folder, f"Accounts.txt")
text_file2 = os.path.join(text_files_folder, f"AltManagerLogin.txt")

settings_file = os.path.join(User_folder, "settings.json")

# ReadFile both json & more
def readfile(datafile):
    try:
        with open(datafile, "r") as file:
            data = json.load(file)
        return data
    except:
        with open(datafile, "r") as file:
            return file.read()

# Write files both Json & more
def writefile(datafile, data):
    try:
        with open(datafile, "w") as file:
            json.dump(data, file, indent=4)
    except json.decoder.JSONDecodeError:
        with open(datafile, "w") as file:
            file.write(data)

def makeAccountFiles():
    if not os.path.exists(text_files_folder):
        os.makedirs(text_files_folder)

    if not os.path.exists(text_file):
        open(text_file, "w").close()

    if not os.path.exists(text_file2):
        open(text_file2, "w").close()

# Save account information to text file
def save_account_info(account_info):
    with open(text_file, 'a') as file:
        file.write(f"Username: {account_info[1]}\nPassword: {account_info[2]}\nCookie: {account_info[0]}\n\n\n")

# Save login information for AltManager
def save_altmanager_login(item, current_accounts):
    for data in current_accounts:
        with open(text_file2, 'a') as file:
            file.write(f"{data[1]}:{data[2]}: Item {item}\n")

    current_accounts.clear()
