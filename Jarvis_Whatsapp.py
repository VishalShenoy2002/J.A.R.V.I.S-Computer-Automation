import pyautogui
import time
from JARVIS.Jarvis_basic import takecommand
class WhatsApp:
    def __init__(self):
        pass
    
    def Open_Whatsapp(self):
        pyautogui.moveTo(180,1079,duration=0.5)
        pyautogui.click()
        pyautogui.typewrite('WhatsApp',interval=0.25)
        pyautogui.press('enter')
        time.sleep(10)
        pyautogui.press('esc')
        time.sleep(60)
    def Search_contact(self,contact):
        pyautogui.moveTo(357,163)
        pyautogui.click()
        pyautogui.typewrite(contact,interval=0.25)
        pyautogui.press('enter')

    def Type_message(self,message):
        time.sleep(5)
        pyautogui.moveTo(1264,967)
        pyautogui.click()
        pyautogui.typewrite(message,interval=0.25)
    def Send_message(self):
        pyautogui.press('enter')


# __main__
wt=WhatsApp()
while True:
    print('Listening')
    ask=takecommand()
    if 'open whatsapp' in ask.lower():
        
        wt.Open_Whatsapp()

