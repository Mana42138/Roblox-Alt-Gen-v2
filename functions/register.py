from .utility.status import *
from .utility.filesys import *
from .utility.processes import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from classes import *

import secrets
import time

days = [str(i + 1) for i in range(10, 28)]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
years = [str(i + 1) for i in range(1980, 2004)]

ActualWindows = 0
current_accounts = []
program_name = "RobloxPlayerBeta.exe"
roblox_url = "https://www.roblox.com/"

#Username generator
def gen_user(first_names, last_names):
    status("Generating a username...")
    first = secrets.choice(first_names)
    last = secrets.choice(last_names)
    full = f"{first}{last}_{secrets.choice([i for i in range(1, 999)]):03}"
    return full

def create_account(url, first_names, last_names):
        global ActualWindows
        # Config
        settings = readfile(settings_file)
        AUTO_LAUNCH = settings["AUTO_LAUNCH"]
        PASSWORD = settings["PASSWORD"]
        SHOW_CODES = settings["SHOW_CODES"]
        GAME_ID = settings["GAME_ID"]
        AUTO_CLOSE_ROBLOX = settings["AUTO_CLOSE_ROBLOX"]

        if AUTO_CLOSE_ROBLOX:
            terminate_process(program_name)

        status("Starting to create an account...")
        cookie_found = False
        username_found = False
        elapsed_time = 0
        status("Initializing webdriver...")
        driver = webdriver.Chrome()
        driver.set_window_size(1200, 800)
        driver.set_window_position(0, 0)
        # driver.minimize_window()
        driver.get(url)
        time.sleep(2)
        
        # HTML items
        status("searching for items on the website")
        try:
            accept_button = driver.find_element(By.CLASS_NAME, "btn-cta-lg")
            accept_button.click()
        except:
            pass
            
        username_input = driver.find_element("id", "signup-username")
        username_error = driver.find_element("id", "signup-usernameInputValidation")
        password_input = driver.find_element("id", "signup-password")
        day_dropdown = driver.find_element("id", "DayDropdown")
        month_dropdown = driver.find_element("id", "MonthDropdown")
        year_dropdown = driver.find_element("id", "YearDropdown")
        male_button = driver.find_element("id", "MaleButton")
        female_button = driver.find_element("id", "FemaleButton")
        register_button = driver.find_element("id", "signup-button")

        status("Selecting day...")
        Selection = Select(day_dropdown)
        Selection.select_by_value(secrets.choice(days))

        status("Selecting month...")
        Selection = Select(month_dropdown)
        Selection.select_by_value(secrets.choice(months))

        status("Selecting year...")
        Selection = Select(year_dropdown)
        Selection.select_by_value(secrets.choice(years))

        while not username_found:
            status("Selecting username...")
            username = f"{gen_user(first_names, last_names)}"
            username_input.clear()
            username_input.send_keys(username)
            if username_error.text.strip() == "":
                username_found = True
        
        status("Selecting password...")
        password = PASSWORD
        password_input.send_keys(password)
        time.sleep(0.3)
        
        status("Selecting gender...")
        gender = secrets.choice([1,2])
        if gender == 1:
            male_button.click()
        else:
            female_button.click()
        time.sleep(0.5)

        status("Registering account...")
        register_button.click()
        time.sleep(3)

        # Wait until the account creation limit is reset
        try:
            driver.find_element("id", "GeneralErrorText")
            # driver.quit()
            for i in range(15*60):
                status(f"Limit reached, waiting... {i+1}/{15*60}")
                time.sleep(1)
        except:
            pass
            
        # Wait until the cookie is found or the maximum time has passed
        while not cookie_found and elapsed_time < 180:
            status("Waiting for the cookie...")
            time.sleep(.5)
            elapsed_time += 3
            for cookie in driver.get_cookies():
                if cookie.get('name') == '.ROBLOSECURITY':
                    cookie_found = True
                    break
        if cookie_found:
            status("Cookie found...")
            result = [cookie.get('value'), username, password]
            save_account_info(result)
            driver.minimize_window()
            
            if result is not None:
                status("Successfully created!")
                if AUTO_LAUNCH:
                    Manager = AccountLaunch(result[0], str(GAME_ID), VIP=False, privateServerLink="nop")
                    ticket = Manager.get_authentication_ticket()
                    job_id = Manager.job_id()
                    
                    status("Launching Roblox...")
                    Manager.launch_roblox(ticket, job_id)

            if SHOW_CODES:
                status(f"##Codes## \n\n")
                codes_list = get_codes()
                if codes_list:
                    for v in codes_list:
                        print(v)

            current_accounts.append(result)

        return result