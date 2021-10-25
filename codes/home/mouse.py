import win32api as win
import random, time, sys
"""
#get mouse x,y position
pos = win.GetCursorPos()

#move mouse
pos = (200, 200)
win.SetCursorPos(pos)
"""
try:
    while True:
        x = random.randint(1, 100)
        y = random.randint(1,100)
        pos = (x,y)
        win.SetCursorPos(pos)
        time.sleep(10)

except KeyboardInterrupt:
    sys.exit()
