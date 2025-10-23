import pyautogui as pg 
from time import sleep

# pg.mouseInfo()



pg.press("win")
pg.write("chrome")
pg.press("enter")
pg.moveTo(691,58, duration=1)
pg.click()
pg.write("jogos 360")
pg.press("enter")

pg.moveTo(308,348, duration=1)
pg.click()
pg.click()

pg.moveTo(944,575, duration=2)
pg.click()


pg.moveTo(629,526, duration=2)
pg.click()
