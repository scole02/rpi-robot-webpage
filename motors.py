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

    motorNum = 0
    direction = 1
    level = 128
    for i in range(6):
        my_driver.set_drive(i, direction, level)
    
    time.sleep(1.0)
    level = 0
    
    for i in range(6):
        my_driver.set_drive(i, direction, level)

    my_driver.set_drive(motorNum, direction, level)


if __name__ == "__main__":
    main()
