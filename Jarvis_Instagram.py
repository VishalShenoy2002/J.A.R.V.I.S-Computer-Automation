import pyautogui
import time
class Instagram:
    def __init__(self):
        pass

    def Open_Instagram(self):
        pyautogui.moveTo(180,1057,duration=0.5)
        pyautogui.click()
        pyautogui.typewrite('Instagram',interval=0.25)
        pyautogui.press('enter')
        time.sleep(10)
        pyautogui.press('esc')

    def goto_DM(self):
        time.sleep(5)
        pyautogui.moveTo(1448,96,duration=0.5)
        pyautogui.click()

    def search_user_in_DM(self,user):
        time.sleep(3)
        pyautogui.moveTo(1163,730,duration=0.5)
        pyautogui.click()
        pyautogui.typewrite(user,interval=0.25)
        pyautogui.moveTo(958,465,duration=0.5)
        pyautogui.click()
        pyautogui.moveTo(1210,322,duration=0.5)
        pyautogui.click()

    def write_DM(self,content):
        time.sleep(2)
        pyautogui.typewrite(content,interval=0.25)
        pyautogui.press('enter')

    def goto_home_screen(self):
        pyautogui.moveTo(1372,84,duration=0.5)
        pyautogui.click()
    
    def check_story(self):
        pyautogui.moveTo(438,264,duration=0.5)
        pyautogui.click()

    def close_story(self):
        pyautogui.moveTo(1229,196)
        pyautogui.click()

    def goto_Explore(self):
        pyautogui.moveTo(1509,90,duration=0.5)
        pyautogui.click()

    def goto_likespage(self):
        pyautogui.moveTo(1577,90)
        pyautogui.click()

    def goto_Profile(self):
        pyautogui.moveTo(1646,90,duration=0.5)
        pyautogui.click()
        pyautogui.moveTo(1541,160,duration=0.5)
        pyautogui.click()

    def goto_saved_scrren(self):
        pyautogui.moveTo(1646,90,duration=0.5)
        pyautogui.click()
        pyautogui.moveTo(1440,214,duration=0.5)
        pyautogui.click()

    def close_insta(self):
        pyautogui.hotkey('alt','f4')

# __main__ 
i=Instagram()
i.Open_Instagram()
# i.goto_home_screen()
# i.goto_Explore()
# time.sleep(2.5)
# i.goto_likespage()
# time.sleep(2.5)
i.goto_Profile()
time.sleep(10)
# i.close_insta()
