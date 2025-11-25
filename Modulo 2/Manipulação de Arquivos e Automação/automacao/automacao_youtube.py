import pyautogui as pg 
from time import sleep

# pg.mouseInfo()



pg.press("win")
pg.write("chrome")
pg.press("enter")
pg.moveTo(691,58, duration=1)
pg.click()
pg.write("www.youtube.com")
pg.press("enter")

sleep(2)

pg.press(";")
pg.write("Vampiro de madureira")
pg.press("enter")
pg.moveTo(745,672, duration=1)
pg.click()





