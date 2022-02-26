from time import sleep
import pyautogui
import cv2


# 111,609       rectbox
# 420,90         左上角
# 1385,1045     右下角
# 1080,490
# 1188,378     上一级文件夹
# 840,409       annotation/双击
# 129,527       保存xml
#1264,725
# 131,324       nextimage

#rectbox，左上角拖拽至右下角，点击确定，保存xml，上一级文件夹，双击annotation，save，nextimage
# print(pyautogui.position())
time = 0.2
# sleep(5)
for i in range(445):
    k = cv2.waitKey(1)
    pyautogui.click(111,609)    # 111,609       rectbox
    sleep(time)
    pyautogui.moveTo(420,90,duration=time) # 420,90         左上角
    sleep(time)
    pyautogui.dragTo(1385,1045) # 1385,1045     右下角
    sleep(time)
    pyautogui.click(1080,490)# 1080,490
    sleep(time)
    pyautogui.click(129,527)# 129,527       保存xml
    sleep(time)
    pyautogui.click(1188,378)# 1188,378     上一级文件夹
    sleep(time)
    pyautogui.click(840,409)
    # pyautogui.click(840,409, clicks=2,interval=0.1,duration=0.5)# 840,409       annotation/双击
    sleep(time)
    pyautogui.click(1264,725, clicks=2,interval=0.1,duration=time)
    # pyautogui.click(1264,725)
    sleep(time)
    pyautogui.click(131,324)# 131,324       nextimage
    sleep(time)
    if k == 27:
        break