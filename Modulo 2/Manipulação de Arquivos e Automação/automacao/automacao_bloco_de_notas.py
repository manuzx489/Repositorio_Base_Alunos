import pyautogui as pg 
from time import sleep

# pg.mouseInfo()



pg.press("win")
pg.write("bloco de notas")
pg.press("enter")
pg.moveTo(365,73, duration=1)
pg.click()
sleep(2)
pg.write("Ola mundo", interval=0.5)
pg.press("enter")
pg.write("tudo bem?")


