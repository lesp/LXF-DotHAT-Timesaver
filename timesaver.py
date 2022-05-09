import time
import math
import webbrowser as wb
import dothat.backlight as backlight
import dothat.lcd as lcd
import dothat.touch as nav
from dot3k.menu import Menu, MenuOption
from plugins.text import Text

x = 0
def lxf():
    lcd.clear()
    backlight.rgb(255, 0, 0)
    lcd.write("Linux Format")
    wb.open_new_tab("https://linuxformat.co.uk")

def th():
    lcd.clear()
    backlight.rgb(0, 255, 0)
    lcd.write("Linux Format")
    wb.open_new_tab("https://tomshardware.com")
    
def bgl():
    lcd.clear()
    backlight.rgb(0, 0, 255)
    lcd.write("Linux Format")
    wb.open_new_tab("https://bigl.es")
    
menu = Menu(
    structure={
        "Linux Format": lxf,
        "Tom's Hardware": th,
        "Bigles": bgl
    },
    lcd=lcd,
    idle_handler=lxf,
    idle_timeout=30,
    input_handler=Text())

nav.bind_defaults(menu)

while True:
    menu.redraw()
    time.sleep(0.05)
    x += 1
    backlight.sweep((x % 360) / 360.0)
    time.sleep(0.01)