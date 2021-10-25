from ahk import AHK
import time

ahk = AHK()
ahk.mouse_position
ahk.click(1252, 17)

ahk.click(61, 273)
ahk.type('one')
ahk.click(60, 294)
ahk.type('two')
ahk.click(64, 316)
ahk.type('three')

time.sleep(3)

ahk.mouse_position = (61, 273)
ahk.mouse_drag(64, 316)


ahk.run_script('send ^c')
#ahk.send("^c")

time.sleep(3)

ahk.click(245, 274)

#ahk.send("^v")
#https://www.autohotkey.com/boards/viewtopic.php?t=3626
#https://www.autohotkey.com/docs/Hotkeys.htm

ahk.run_script('send ^v')