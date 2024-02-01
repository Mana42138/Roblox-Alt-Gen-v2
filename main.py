from classes import *
from functions.register import *
import time, threading

first_names, last_names = get_usernames()

makeAccountFiles()

Settings_Setup()

settings = readfile(settings_file)
if settings["MULTI_ROBLOX_THREADING"]:
    multi_roblox()

threading.Thread(target=autocopy).start()

# Function for generating accounts
def main_creation():
    settings = readfile(settings_file) 
    MULTI_ROBLOX_THREADING = settings["MULTI_ROBLOX_THREADING"]
    MAX_WINDOWS = settings["MAX_WINDOWS"]

    if MULTI_ROBLOX_THREADING:
        global ActualWindows
        
        for i in range(MAX_WINDOWS):
            ActualWindows += 1
            account_thread = threading.Thread(target=create_account, args=(roblox_url, first_names, last_names))
            account_thread.start()
        time.sleep(1)
    else:
        create_account(roblox_url, first_names, last_names)
    item = input("")
    save_altmanager_login(item, current_accounts)
    
    if readfile(settings_file)["AUTO_CLOSE_ROBLOX"]:
        terminate_process(program_name)

if __name__ == "__main__":
    while True:
        main_creation()
