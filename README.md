# Roblox Account Generator

Welcome to the Roblox Account Generator! This Python script is designed to automate the process of creating Roblox accounts with various features to enhance your account creation experience.

## Features

### 1. Auto Copy Codes (Elemental Dungeons Only)
This feature allows the script to automatically copy codes specifically designed for Elemental Dungeons, streamlining the process of redeeming in-game items.

### 2. Launch The Account
Once the account creation is complete, the script can automatically launch the newly created Roblox account, saving you time and effort.

### 3. Fast Account Creation with Selenium
Utilizing the power of Selenium, this script ensures fast and efficient account creation. Selenium is a powerful tool for automating web browsers, enabling seamless interaction with the Roblox registration page.

### 4. Multi-Account Creation with Multi-Roblox
For users who need to create multiple Roblox accounts simultaneously, the script offers multi-account creation functionality. This is particularly useful for those managing multiple accounts or participating in various Roblox activities.

## Getting Started

1. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```

2. Import the necessary classes and functions from the provided modules.

   ```python
   from classes import *
   from functions.register import *
   ```

3. Customize your account creation settings using the `Settings_Setup()` function.

4. Run the script using the provided main function.

   ```python
   if __name__ == "__main__":
       main_creation()
   ```

## Note

- Multi-Roblox Threading is still in BETA. Please use it with caution and provide feedback for improvement.

Feel free to explore and modify the script based on your specific needs. Happy account creating!