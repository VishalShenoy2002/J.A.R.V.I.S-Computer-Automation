import pyautogui
import webbrowser
import time

class Youtube:
    def __init__(self):
        pass

    def OpenYoutube(self):
        webbrowser.open('https://www.youtube.com/')

    def YoutubeSearch(self,search_content):
        pyautogui.moveTo(625,189,duration=0.5)
        pyautogui.click()
        pyautogui.typewrite(search_content,interval=0.25)
        pyautogui.press('enter')

    def goto_History(self):
        pass

    def goto_Trending(self):
        pass

    def goto_Home(self):
        pass
    def goto_myChannel(self):
        pass

    def Switch_User(self):
        pass



