import msvcrt
import time
import pyautogui
from win32gui import FindWindow, GetWindowRect


windowSize=[]
windowName = input()
window_handle = FindWindow(None, windowName)
window_rect = GetWindowRect(window_handle)
for i in range(0,4):
    windowSize.append(window_rect[i])

print(windowSize)

getFish = []
fixRod = []

ratio = []

f = open('GetFishProcess.txt',"r")
Getprocess = f.read().split()
f.close()
if len(Getprocess) > 1:
    print("True")
    for i in range (0,len(Getprocess),2):
        getFish.insert(i,[int(Getprocess[i]),int(Getprocess[i+1])])
else:
    count = 0
    print("Di chuột và bấm z để lấy nút thả cần và rút cần")
    while count < 2:
        s = msvcrt.getch()
        if s != 'a':
            getFish.insert(count,[pyautogui.position().x,pyautogui.position().y])
            count += 1
        else:
            break
    f = open('getFishProcess.txt','w')
    for i in range (0,len(getFish)): 
        for j in range (0,2):
            f.write(str(getFish[i][j]) + " ")
    f.close()

print(getFish)

f2 = open('FixRodProcess.txt',"r")
Fixprocess = f2.read().split()
f2.close()
if len(Fixprocess) > 1:
    for i in range (0,len(Fixprocess),2):
        fixRod.insert(i,[int(Fixprocess[i]),int(Fixprocess[i+1])])
else:
    count2 = 0
    print("Di chuột và bấm z để lấy quá trình sửa cần")
    while count2 < 7:
        s2 = msvcrt.getch()
        if s2 != 'a':
            fixRod.insert(count2,[pyautogui.position().x,pyautogui.position().y])
            count2 += 1
        else:
            break
    f2 = open('FixRodProcess.txt','w')
    for i in range (0,len(fixRod)): 
        for j in range (0,2):
            f2.write(str(fixRod[i][j]) + " ")
    f2.close()

print(fixRod)

def checkFish(windowSize):
    screenShot = pyautogui.screenshot(region=(windowSize[0],windowSize[1],windowSize[2],windowSize[3]))
    width, height = screenShot.size 
    fish_check = 0
    for x in range( 0, width, 5):
            for y in range(0, height, 5):
                r,g,b = screenShot.getpixel((x,y))
                if r == 14 and g == 24 and b == 59:
                    fish_check = fish_check + 1
                elif r == 14 and g == 38 and b == 70:
                    fish_check = fish_check + 1
                elif r == 0 and g == 97 and b == 140:
                    fish_check = fish_check + 1
                elif r == 104 and g == 84 and b == 111:
                    fish_check = fish_check + 1
    return fish_check

def Fishing(getFish,windowSize):
    pyautogui.click(getFish[0][0],getFish[0][1])
    time.sleep(0.5)
    while True:
        count = 0
        screenShot = pyautogui.screenshot(region=(round(windowSize[2]*0.6),windowSize[1],round(windowSize[2]*0.4),windowSize[3]))
        width, height = screenShot.size
        for x in range( 0, width, 5):
            for y in range(0, height, 5):
                r,g,b = screenShot.getpixel((x,y))
                if r == 65 and g ==197 and b == 243:
                    count += 1
                    if count == 10:
                        pyautogui.click(x + round(windowSize[2]*0.6),y + windowSize[1])
                        break
            if count == 10: break
        if count == 10: break
    time.sleep(0.5)
    pyautogui.click(getFish[1][0],getFish[1][1])

def FixRod():
    for i in range (0,len(fixRod),2):
        pyautogui.click(fixRod[i][0],fixRod[i][1])
        time.sleep(0.5)

while True:
    check = checkFish(windowSize)
    if check > 0:
        print(check)
        time.sleep(1)
        fishSize = checkFish(windowSize)
        if fishSize > 2:
            print(fishSize)
            while True:
                if pyautogui.locateOnScreen("detected1.png",region=(windowSize[0],windowSize[1],windowSize[2],round(windowSize[3]/2)),grayscale=True, confidence=0.8) != None: 
                    print("detected")
                    Fishing(getFish,windowSize)
                    break
                if pyautogui.locateOnScreen("detected3.png",region=(windowSize[0],windowSize[1],windowSize[2],round(windowSize[3]/2)),grayscale=True, confidence=0.8) != None or pyautogui.locateOnScreen("detected6.png",region=(windowSize[0],windowSize[1],windowSize[2],round(windowSize[3]/2)),grayscale=True, confidence=0.8) != None or  pyautogui.locateOnScreen("detected5.png",region=(windowSize[0],windowSize[1],windowSize[2],round(windowSize[3]/2)),grayscale=True, confidence=0.8) != None: 
                    pyautogui.click(getFish[1][0],getFish[1][1])
                    break
    if pyautogui.locateOnScreen("detected4.png",region=(windowSize[0],windowSize[1],windowSize[2],windowSize[3]),grayscale=True, confidence=0.5) != None : 
        print("fixRod")
        FixRod()
