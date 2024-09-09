
import fire

from .utils import *
from .bigip_pyautogui import *

take_screen_shot = lambda debug: screen_shot()  if debug else None 

def big(debug=False, sleep_time=2):
    """
    Automates the BIG-IP Edge Client opening and entering credentials.
    
    Args:
    --debug (bool): Enables saving screenshots at various steps for debugging.
    --sleep_time (int): sleep execution for n swc during execution

    Process:
    - Opens the BIG-IP Edge Client.
    - Takes screenshots if debug is enabled.
    - Locates the "Connect" button, clicks it, and enters the user's credentials.
    - Handles the second password prompt if necessary.
    """
    print(f"{debug=}")
    
    user.get_password()

    app = MacOSApplicationManager('BIG-IP Edge Client')
    app.open()

    print(f"{app.app_name} is running...")
    sleep(5) #  let the app start up

    take_screen_shot(debug)

    #search connect image
    image_path = get_abs_path('ref_image/1/1.png')
    loc = search_image2center(image_path)

    loc = get_gui_loc(loc) # get the scaled location wrt pyautogui
    
    if debug:print(f"Connect button location wrt pyautogui @{loc=}")

    if loc:
        # move to the connect button, click and wait for password promt
        pyautogui.moveTo(loc[0], loc[1], 0.01 )
        pyautogui.click()

        sleep(sleep_time) # wait for it to appear
        take_screen_shot(debug)
        

        #enter username, tab, pwd and enter
        enter_keys(user.username)
        tab()
        enter_keys(user.password)
        enter()

        #wait for 2nd time pwd entering
        sleep(sleep_time)
        take_screen_shot(debug)
        

        enter_keys(user.password)
        enter()
        sleep(sleep_time)
        take_screen_shot(debug)
        
    else:
        print("could not find the connect button😔!!! \ntry some debug 🤷‍♂️.")

def main():
    fire.Fire(big)

if __name__ == '__main__':
    main()