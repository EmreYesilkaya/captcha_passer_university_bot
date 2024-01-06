import time
import pyautogui

# Set PyAutoGUI fail-safe and pause settings
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3
file_path = 'list\\pswd1.txt'

# Placeholder for student number
student1 = '' # The student number must be entered here
line_index = 0

# Read passwords from file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Open Windows start menu and search for Google
pyautogui.hotkey('win')
pyautogui.typewrite('google')
pyautogui.press('enter')
pyautogui.typewrite('')#school service web site name 

# Function to get the next password from the file
def get_next_password():
    global line_index
    if line_index < len(lines):
        password = lines[line_index].strip()
        line_index += 1
        return password
    else:
        return None

# Locate the Google icon
google = None
while google is None:
        print('Searching for Google')
        google = pyautogui.locateCenterOnScreen('photo\\google.PNG', grayscale=True, confidence=0.9)
        pyautogui.click(google, button='left', clicks=1)

print('Entering site')
pyautogui.write('')#school service web site name 
pyautogui.press('enter')

# Locate the OBS icon
baskent = None
while baskent is None:
    baskent = pyautogui.locateCenterOnScreen('photo\\obs.PNG', grayscale=True, confidence=0.9)
    pyautogui.click(baskent, clicks=1)
    time.sleep(1)
    print('Searching for buobs')

# Function to perform login
def login1():
    pswd1 = get_next_password()
    if pswd1 is None:
        print("No more passwords in the file.")
        return

    # Locate the captcha
    captcha = None
    while captcha is None:
        captcha = pyautogui.locateCenterOnScreen('photo\\captcha.PNG', grayscale=False, confidence=0.5)
        print('Captcha found')
        pyautogui.click(captcha, button='right', clicks=1)

    # Various steps in the login process, locating elements and interacting with them
    # ...

    print('Reached this point')

    # More steps in the login process
    # ...

login1()

# Loop to handle login errors
while True:
    error = pyautogui.locateCenterOnScreen('photo\\error2.png', confidence=0.33)
    if error is not None:
        print('Error found. Retrying login...')
        login1()
    else:
        print('Hel')

