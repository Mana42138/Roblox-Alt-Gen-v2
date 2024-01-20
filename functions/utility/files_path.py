import os, sys
files__path = os.path.dirname(os.path.abspath(sys.argv[0]))
User_folders = os.path.join(files__path, "User")

def files_path():
    return os.path.dirname(os.path.abspath(sys.argv[0]))

def User_folder():
    if not os.path.exists(User_folders):
        os.makedirs(User_folders)
    return User_folders

