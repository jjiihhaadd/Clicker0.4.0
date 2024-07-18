import os
import keyboard
import mouse
import time

TXT = (
    "#To get mouse position press [ ESC + P ] \n#To make Right click press [ > ] \n#To make Left click press [ < ]\n#To Set speed press [ ESC + S ]  \n#To clear Screen [ ESC + C ] \n#For "
    "Help press [ ESC + ? ] \n#About [ ESC + A ] \n#To exit press [ ESC + X ]")

print(TXT)

ABT = ("\n\nAbout:\n\nDeveloper: Tension_IDK [Jihad] \nScripted And Build with python. \nUsed Module's: Os, Keyboard, Mouse, Time \nConverted Python script to EXE file using: Auto_Py_To_Exe_Master")

HLP = "\n\n\n#To set new HOTKEY:\n#press[ ESC + L ] for LEFT click.\n#press[ ESC + R ] for right click"

LHK = ','

RHK = '.'

SLP = 0.0

while True:

    POST = keyboard.is_pressed(' + p')
    MP = mouse.get_position()
    LC = keyboard.is_pressed(LHK)
    RC = keyboard.is_pressed(RHK)
    EXT = keyboard.is_pressed(" + x")
    CLR = keyboard.is_pressed(" + c")
    HL = keyboard.is_pressed(" + ?")
    LK = keyboard.is_pressed(" + l")
    RK = keyboard.is_pressed(" + r")
    SPD = keyboard.is_pressed(" + s")
    ABK = keyboard.is_pressed(" + a")


    if POST:
        print(MP)
        time.sleep(0.2)

    elif SPD:
        slp = input("Enter the Speed(sec):")
        try:
            slp = float(slp)
            SLP = slp
            print("Speed set to:", SLP, " sec")
        except ValueError:
            if not type(slp) is float or int:
                slp = 0.0
                print("Please Enter Integer Data!!!\nTry again.")
                

    elif LC:
        time.sleep(SLP)
        mouse.click("left")

    elif RC:
        time.sleep(SLP)
        mouse.click("right")

    elif CLR:
        os.system('CLS')
        print(TXT)
        time.sleep(0.2)

    elif HL:
        print(HLP)
        time.sleep(0.5)
    
    elif ABK:
        time.sleep(0.5)
        print(ABT)

    elif LK:
        time.sleep(0.5)
        LHK = input("\nSelect KEY for Left Click:")
        if len(LHK) == 1:
            print("Left Click set to>", LHK)
        else:
            print("Please Enter a valid Key !!")
            LK()

    elif RK:
        time.sleep(0.5)
        RHK = input("\nSelect KEY for Right Click:")
        if len(RHK) == 1:
            print("Right Click set to>", RHK)
        else:
            print("Please Enter a valid Key !!")
            RK()

    elif EXT:
        break
