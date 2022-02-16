import pyautogui
import time
import Save


def calibration():
    print('hold you coursor in the middle of magazine name for a 3-5 seconds')
    time.sleep(6)
    currentMouseX, currentMouseY = pyautogui.position()

    pyautogui.alert(
        f'Coordinates of your item: {currentMouseX} and {currentMouseY} \n Press "ok" to continue')
    time.sleep(1)
    print('Make Right click on the magazine and hold your coursor in middle of "unload" row for 3-5 sec')
    time.sleep(7)
    currentMouseXX, currentMouseYY = pyautogui.position()
    pyautogui.alert(
        f'Coordinates of your item: {currentMouseXX} and {currentMouseYY} \n Press "ok" to continue')
    time.sleep(1)
    right_click_pos, left_click_pos = [
        currentMouseX, currentMouseY], [currentMouseXX, currentMouseYY]
    answer = input(
        'Do you want to save these coordinates? y - Yes, n - No  : ')
    if answer.lower() == 'y':
        coordinates = right_click_pos, left_click_pos
        Save.save_saves('save_reloading', str(coordinates))
    else:
        print('your choice...')
        return right_click_pos, left_click_pos
    return right_click_pos, left_click_pos
