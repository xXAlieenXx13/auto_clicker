import pyautogui
import time
import keyboard

# Delay before the autoclicker starts (in seconds)
start_delay = 1

# Interval between each click (in seconds)
click_interval = 1/5000000

# Number of clicks (0 for infinite)
num_clicks = 0 # Set to 0 for infinite

# Delay to stop the script gracefully
graceful_exit_delay = 2

# Initial state
running = False

def toggle_running():
    global running
    running = not running
    if running:
        print("Autoclicker started.")
    else:
        print("Autoclicker stopped.")

# Set up F8 key to toggle the autoclicker
keyboard.add_hotkey('F8', toggle_running)

def auto_clicker(interval):
    print(f"Waiting for {start_delay} seconds before starting...")
    time.sleep(start_delay)
    print("You can press F8 to toggle the autoclicker on/off.")

    while True:
        if running:
            pyautogui.click()
            time.sleep(interval)
        else:
            time.sleep(0.5)
try:
    auto_clicker(click_interval)
except KeyboardInterrupt:
    print(f"\nAutoclicker interrupted. Exiting in {graceful_exit_delay} seconds.")
    time.sleep(graceful_exit_delay)
