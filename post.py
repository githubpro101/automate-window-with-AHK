from ahk import AHK
import time
from ahk.window import Window

ahk = AHK()

ahk.mouse_position

#minimize vs code tab
ahk.click(1252, 17)

#go to internet and search linkedin to go there
ahk.click(711, 748)
time.sleep(3)
ahk.click(180,51)
ahk.type('https://www.linkedin.com/feed/')
ahk.key_press('Enter')
time.sleep(5)

#write text for post
ahk.click(487, 215)
time.sleep(3)
ahk.type('Good Morning, I am feeling great as I fully automated the weekly report process including the posting of the article')
time.sleep(5)

#add file
ahk.click(501,692)
ahk.click(582,174)
time.sleep(5)
#find file to upload
ahk.click(303,290)
ahk.type('C:\\Users\\Jarvis\\Desktop\\New folder\\Python\\covidreport')
ahk.key_press('Enter')
time.sleep(5)
ahk.click(522,296)
time.sleep(3)
ahk.type('CovidReport')
ahk.key_press('Enter')
time.sleep(5)
ahk.double_click(368,372)
time.sleep(8)

#title the document
ahk.click(476,187)
ahk.type('Covid Analytics Report')

#post
ahk.click(923,663)