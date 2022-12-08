#!/usr/bin/python

import qwiic_scmd
import time

def main():
    d1 = qwiic_scmd.QwiicScmd(0x5d)
    d2 = qwiic_scmd.QwiicScmd(0x58)
    d3 = qwiic_scmd.QwiicScmd(0x5b)
    d1.begin()
    time.sleep(0.1)
    d2.begin()
    time.sleep(0.1)
    d3.begin()
    time.sleep(0.1)
    print("Drivers Initalized.")

    d1.enable()
    time.sleep(0.1)
    d2.enable()
    time.sleep(0.1)
    d3.enable()
    time.sleep(0.1)
    print("Motors Enabled")
    time.sleep(0.1)

    # so motors all turn the same direction
    d1.inversion_mode(1, 1)
    d2.inversion_mode(0, 1)
    d3.inversion_mode(1, 1)

    while True:
        level = int(input("Enter level: "))
        dur = float(input("Enter duration: "))
        if dur < 0 or dur > 4:
            print("duration too short or too long")
            return
        # left
        d1.set_drive(1, 0, level)
        d2.set_drive(0, 0, level)
        d3.set_drive(0, 0, level)
        
        # right
        d1.set_drive(0, 0, level * -1)
        d2.set_drive(1, 0, level * -1)
        d3.set_drive(1, 0, level * -1)
        
        time.sleep(dur)
        
        for i in range(2):
            d1.set_drive(i, 0, 0)
            d2.set_drive(i, 0, 0)
            d3.set_drive(i, 0, 0)

    

if __name__ == "__main__":
    main()
