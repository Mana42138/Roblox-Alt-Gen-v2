from .filesys import *
import threading
import keyboard
import pyperclip

data = readfile(settings_file)

COPY_CODES_KEY = data["COPY_CODES_KEY"]

word_list = [
"UPD4",
"SORRYDELAYS3",
"100MVISITSTHANKS",
"SEASONONE",
"SORRYDELAYS2",
"SORRYDELAYS:(",
"BETA",
"XMAS",
"FOLLOWER",
]

index = 0

# Auto copy codes for spesific games
def copy_next_word(event):
    global index
    if event.name == COPY_CODES_KEY:
        if index < len(word_list):
            word_to_copy = word_list[index]
            index += 1
            pyperclip.copy(word_to_copy)
        else:
            index = 0

def main_copy():
    keyboard.on_press(copy_next_word)

    keyboard.wait('f5')

def autocopy():
    auto_copy = data["AUTO_COPY_CODES"]

    if auto_copy:
        thread_one = threading.Thread(target=main_copy)
        thread_one.start()
