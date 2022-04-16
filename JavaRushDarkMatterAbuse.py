import pyautogui as pg
import time
import progressbar

n=int(input("Сколько монет хотите получить? : "))
print("ОТКРОЙТЕ БРАУЗЕР И ВКЛАДКУ С ОПРОСОМ! У вас есть 15 секунд!")
bar = progressbar.ProgressBar(maxval=n//2+n%2, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
time.sleep(15)
for i in range(n//2+n%2):
    pg.press('f5')
    time.sleep(6)
    pg.scroll(-720)
    time.sleep(2)
    pg.click(768,364)
    time.sleep(1)
    pg.click(588,526) #1
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    pg.click(590,525) #2
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    pg.click(589,579) #3
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    pg.click(586,472) #4
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    pg.click(590,417) #5
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    pg.click(590,471) #6
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    pg.click(586,413) #7
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    pg.click(588,526) #8
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    pg.click(588,579) #9
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    pg.click(589,578) #10
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    pg.click(1472,916)
    time.sleep(1)
    bar.update(i+1)
    time.sleep(0.1)
bar.finish()
print("DONE!")
