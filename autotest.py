#tutorial source: https://pypi.org/project/ahk/
#https://github.com/spyoungtech/ahk#non-python-dependencies
# place I heard autohotkey from: https://en.wikipedia.org/wiki/Comparison_of_GUI_testing_tools

from ahk import AHK
import time
from ahk.window import Window

ahk = AHK()

ahk.mouse_position
ahk.click(1252, 17)

ahk.run_script('run explorer.exe C:\\Users\\Jarvis\\Desktop\\New folder, C:\Windows, max')
#https://www.autohotkey.com/board/topic/100235-cannot-seem-to-maximize-folder-in-windows-explorer/

time.sleep(5)
ahk.double_click(1222, 68)
time.sleep(5)
ahk.type('hello')
