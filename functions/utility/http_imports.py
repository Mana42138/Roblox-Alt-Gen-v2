from .status import *
from requests import *

def get_usernames():
    status("Getting first names...")
    first_names_response = get("https://raw.githubusercontent.com/Mana42138/Gen-RX/main/firstnames.txt")
    status("Getting last names...")
    last_names_response = get("https://raw.githubusercontent.com/Mana42138/Gen-RX/main/lastnames.txt")

    if first_names_response.status_code == 200 and last_names_response.status_code == 200:
        first_names = list(set(first_names_response.text.splitlines()))
        last_names = list(set(last_names_response.text.splitlines()))
        return first_names, last_names
    else:
        status("Name loading failed. Re-Execute the script.")
        return False, False

def get_codes():
    codes = get("https://raw.githubusercontent.com/Mana42138/Gen-RX/main/codes.txt")
    if codes.status_code != 200:
        status("Code request failed. Re-Executing")
        return None
    return codes

