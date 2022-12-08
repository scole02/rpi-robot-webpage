#!/usr/bin/python

import qwiic_scmd
import time

def main():
    my_driver = qwiic_scmd.QwiicScmd()
    if my_driver.connected == False:
        print("Motor Driver not connected. Check Connection.")
        return
    my_driver.begin()
    print("Driver Initalized.")
    time.sleep(0.3)

    my_driver.enable()
    print("Motor Enabled")
    time.sleep(0.3)
           
    direction = 1
    level = 20
    while True:
        motorNum = int(input("Type motorNum(0-5): "))
        if motorNum < 0 or motorNum > 5:
            continue
        my_driver.set_drive(motorNum, direction, level)
        time.sleep(2.0)
        my_driver.set_drive(motorNum, direction, 0)

if __name__ == "__main__":
    main()
