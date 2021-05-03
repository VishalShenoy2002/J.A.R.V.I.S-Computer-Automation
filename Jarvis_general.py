import pyautogui

class OS_Functions:
    def __init__(self):
        pass

    def increase_volume(self):
        pyautogui.press('volumeup',presses=3)

    def decrease_volume(self):
        pyautogui.press('volumedown',presses=3)

    def mute(self):
        pyautogui.press('volumemute',presses=3)

    def capslock(self):
        pyautogui.press('capslock')
    
    def pgup(self):
        pyautogui.press('pgup')

    def page_down(self):
        pyautogui.press('pgdn')

    def screen_record(self):
        pyautogui.hotkey('win','alt','r')

    def screenshot(self):
        pyautogui.hotkey('win','alt','prtsc')

    def show_gamebar(self):
        pyautogui.hotkey('win','g')



class Other_General_Functions:
    def __init__(self):
        pass
    
    def take_printout(self):
        pyautogui.hotkey('ctrl','p')

    def copy_text(self):
        pyautogui.hotkey('ctrl','c')
    
    def paste_text(self):
        pyautogui.hotkey('ctrl','v')

    def save_file(self):
        pyautogui.hotkey('ctrl','s')

    def saveas_file(self):
        pyautogui.hotkey('ctrl','shift','s')
        
    def minmax_screen(self):
        pyautogui.hotkey('win','d')

    def switch_tab(self):
        pyautogui.hotkey('alt','tab')




