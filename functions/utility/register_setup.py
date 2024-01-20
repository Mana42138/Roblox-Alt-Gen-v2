from .filesys import *
from .status import status

settings_file = os.path.join(User_folder(), "settings.json")

def Settings_Setup():
    if not os.path.exists(settings_file):
        status("Initializing first time setup...")
        AUTO_LAUNCH = input("## Auto Launch ##\nWould you like to enable this feature? \n (y/n)")
        if AUTO_LAUNCH=="y":AUTO_LAUNCH=True
        else:AUTO_LAUNCH=False

        SHOW_CODES = input("## Show Codes ##\nWould you like to enable this feature? \n (y/n)")

        if SHOW_CODES=="y":SHOW_CODES=True
        else:SHOW_CODES=False

        AUTO_COPY_CODES = input("## Auto Copy Codes ##\nWould you like to enable this feature? \n (y/n)")

        if AUTO_COPY_CODES=="y":AUTO_COPY_CODES=True
        else:AUTO_COPY_CODES=False

        AUTO_CLOSE_ROBLOX = input("## Auto Close Roblox ##\nWould you like to enable this feature? \n (y/n)")

        if AUTO_CLOSE_ROBLOX=="y":AUTO_CLOSE_ROBLOX=True
        else:AUTO_CLOSE_ROBLOX=False

        COPY_CODES_KEY = input("## Copy Codes Key ##\n Please press the key you want to use: ")

        PASSWORD = input("## PASSWORD ##\n Please type your password: ")

        GAME_ID = input("## GAME_ID ##\n Please type the game id you want to join: ")

        MULTI_ROBLOX_THREADING = input("## Multi Roblox ##\nWould you like to enable this feature? \n (y/n)")

        if MULTI_ROBLOX_THREADING=="y":MULTI_ROBLOX_THREADING=True
        else:MULTI_ROBLOX_THREADING=False

        MAX_WINDOWS = input("## Max Windows ##\n Please type 1 - 3: ")

        if int(MAX_WINDOWS) > 3:
            MAX_WINDOWS = 3

        data = {
            "AUTO_LAUNCH": AUTO_LAUNCH,
            "SHOW_CODES": SHOW_CODES,
            "AUTO_COPY_CODES": AUTO_COPY_CODES,
            "COPY_CODES_KEY": COPY_CODES_KEY.lower(),
            "PASSWORD": PASSWORD,
            "GAME_ID": GAME_ID,
            "AUTO_CLOSE_ROBLOX": AUTO_CLOSE_ROBLOX,
            "MULTI_ROBLOX_THREADING": MULTI_ROBLOX_THREADING,
            "MAX_WINDOWS": int(MAX_WINDOWS)
        }
        writefile(settings_file, data)