
import pyautogui
import sys
import traceback

from .utils import get_abs_path

def search_image2center(image_path):
    """
    Searches for an image on the screen within a given timeout period.
    
    Parameters:
    - image_path (str): The path to the image file to search for on the screen.
    
    Returns:
    - The center coordinates of the found image, or None if the image was not found.
    """
    try:
        image_path = get_abs_path(image_path)
        loc = pyautogui.locateOnScreen(image_path, grayscale=True)
        if loc:
            loc = (loc.left+loc.width/2, loc.top+loc.height/2)
            #print(f"Image found at: {loc=}")
            return loc

    except pyautogui.ImageNotFoundException as e:
        print( f"{image_path=} is not found {screen_shot()}" )
    except Exception as e:
        traceback.print_exc()
        sys.exit(-1)

def enter_keys(text, interval=0.01):
    """
    Simulates typing the given text with a specified delay between key presses.
    Parameters:
    text (str): The text to type.
    interval (float): Delay between key presses in seconds.
    """
    # Add a small delay to switch to the desired window
    #sleep()
    
    # Type the text
    pyautogui.write(text, interval=interval)
def screen_shot():
    global photo_count  # To modify the global photo_count variable
    photo_count += 1
    fn = get_abs_path(f'debug_img/my_screenshot_{photo_count}.png')
    print(f"{photo_count=} @ {fn}")
    # Save the screenshot with the updated count
    pyautogui.screenshot().save(fn)
tab = lambda : pyautogui.press('tab')
enter = lambda : pyautogui.press('enter')
screenshot_size =  pyautogui.screenshot().size
photo_count = 0
gui_size = pyautogui.size()
get_gui_loc = lambda x  : (x[0]/screenshot_size[0] * gui_size.width, x[1]/screenshot_size[1] * gui_size.height)
