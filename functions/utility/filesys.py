import os
import sys
import json

def files_path():
    return os.path.dirname(os.path.abspath(sys.argv[0]))

def User_folder():
    User_folders = os.path.join(files_path(), "User")
    if not os.path.exists(User_folders):
        os.makedirs(User_folders)
    return User_folders

def readfile(datafile):
    try:
        with open(os.path.join(files_path(), datafile), "r") as file:
            data = json.load(file)
        return data
    except:
        with open(os.path.join(files_path(), datafile), "r") as file:
            return file.read()
        
def writefile(datafile, data):
    try:
        with open(os.path.join(files_path(), datafile), "w") as file:
            json.dump(data, file, indent=4)
    except json.decoder.JSONDecodeError:
        with open(os.path.join(files_path(), datafile), "w") as file:
            file.write(data)

def makeAccountFiles():
    Accounts_path = User_folder()
    text_files_folder = os.path.join(Accounts_path, "Accounts")
    text_file = os.path.join(text_files_folder, f"Accounts.txt")
    text_file2 = os.path.join(text_files_folder, f"AltManagerLogin.txt")
    if not os.path.exists(text_files_folder):
        os.makedirs(text_files_folder)

    if not os.path.exists(text_file):
        open(text_file, "w").close()

    if not os.path.exists(text_file2):
        open(text_file2, "w").close()
    