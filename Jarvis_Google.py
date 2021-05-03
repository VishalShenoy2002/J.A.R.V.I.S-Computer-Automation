import pyautogui
import webbrowser
import time

class Google:
    def __init__(self):
        pass
    
    def OpenGoogle(self):
        webbrowser.open('www.google.com')

    def SearchGoogle(self,searchcontent):
        pyautogui.typewrite(searchcontent,interval=0.25)
        pyautogui.press('enter')

    def Close_Google(self):
        pyautogui.hotkey('alt','f4')

class Gmail:
    def __init__(self):
        pass

    def OpenGmail(self):
        webbrowser.open('https://mail.google.com/mail/u/0/?tab=wm&ogbl#inbox')
    
    def ComposeMail(self):
        pyautogui.moveTo(70,301,duration=0.5)
        pyautogui.click()

    def AttachFile(self):
        pyautogui.moveTo(477,918,duration=0.5)
        pyautogui.click()
        
    def Write_and_SendMail(self,email,subject,content):
        time.sleep(4)
        pyautogui.typewrite(email,interval=0.25)
        pyautogui.press('tab')
        pyautogui.moveTo(375,357,duration=0.5)
        pyautogui.click()
        pyautogui.typewrite(subject,interval=0.25)
        pyautogui.press('tab')
        pyautogui.moveTo(1257,582,duration=0.5)
        pyautogui.click()
        pyautogui.typewrite(content,interval=0.25)
        pyautogui.typewrite('\n\n\nSent by J.A.R.I.S',interval=0.25)
        pyautogui.press('tab')
        pyautogui.press('enter')
            
class GoogleDrive:
    def __init__(self):
        pass
    
    def OpenDrive(self):
        webbrowser.open('https://drive.google.com/drive/u/0/my-drive')

    def Add_new_File(self,upload_type='file'):
        if 'file' in upload_type.lower():
            pyautogui.moveTo(99,291,duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(126,381,duration=0.5)
            pyautogui.click()
        elif 'folder' in upload_type.lower():
            pyautogui.moveTo(99,291,duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(114,435,duration=0.5)
            pyautogui.click()
        else:
            print('Wrong Option')
    def OpenRecent(self):
        pyautogui.moveTo(138,502,duration=0.5)
        pyautogui.click()
    def OpenRecent_File(self):
        pyautogui.moveTo(598,582,duration=0.5)
        pyautogui.doubleClick()
    def Download_latest_file(self):
        pyautogui.moveTo(1865,198,duration=0.5)
        pyautogui.click()
        time.sleep(4.5)
        pyautogui.moveTo(1865,271,duration=0.5)
        pyautogui.click()
        
class GoogleMaps:
    def __init__(self):
        pass
    
    def OpenMaps(self):
        webbrowser.open('https://www.google.co.in/maps/')

    def SearchLocation(self,location):
        pyautogui.moveTo(328,210,duration=0.5)
        pyautogui.click()
        pyautogui.typewrite(location,interval=0.25)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.moveTo(74,673,duration=0.5)
        pyautogui.click()
        time.sleep(1.5)
        pyautogui.moveTo(193,432,duration=0.5)
        pyautogui.click()



    def ShowGroceryShop(self):
        pyautogui.moveTo(97,551,duration=0.5)
        pyautogui.click()
    
    def ShowFastFood(self):
        pyautogui.moveTo(235,551,duration=0.5)
        pyautogui.click()
    
    def ShowTakeouts(self):
        pyautogui.moveTo(344,551,duration=0.5)
        pyautogui.click()

    def ShowHotels(self):
        pyautogui.moveTo(473,551,duration=0.5)
        pyautogui.click()
