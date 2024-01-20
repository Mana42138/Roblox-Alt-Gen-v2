import os

def status(text):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1;34m" + text + "\033[0m")