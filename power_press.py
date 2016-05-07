#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep

# for RPi 26pin GPIO (Model A/Model B)
POWER = 18 #GPIO:24
RESET = 22 #GPIO:25
PLED  = 19 #GPIO:10

# for RPi 40pin GPIO (Zero/Model A+/Model B+/Pi2/Pi3)
'''
POWER = 32 #GPIO:12
RESET = 36 #GPIO:16
PLED  = 33 #GPIO:13
'''

def press():
    GPIO.output(POWER,True)
    sleep(0.5)
    GPIO.output(POWER,False)
    return

def press_and_hold():
    GPIO.output(POWER,True)
    sleep(3)
    GPIO.output(POWER,False)
    return

def reset():
    GPIO.output(RESET,True)
    sleep(1)
    GPIO.output(RESET,False)
    return

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(POWER,GPIO.OUT)
    GPIO.setup(RESET,GPIO.OUT)

    # poweron()
    # reset()
    # sleep(3)
    press()

    GPIO.cleanup()

if __name__ == '__main__':
    main()
