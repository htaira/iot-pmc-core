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

def gpio_init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(POWER,GPIO.OUT)
    GPIO.setup(RESET,GPIO.OUT)
    GPIO.setup(PLED,GPIO.IN)

def gpio_cleanup():
    GPIO.cleanup()

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

def cold_boot():
    ret = get_pled_state()
    if ret == 1:
        press_and_hold()
        sleep(3)
    press()
    return

def reset():
    GPIO.output(RESET,True)
    sleep(1)
    GPIO.output(RESET,False)
    return

def get_pled_state():
    ret = GPIO.input(PLED)
    return ret

def power_on():
    ret = get_pled_state()
    if ret == 0:
        press()
    return

def power_off():
    ret = get_pled_state()
    if ret == 1:
        press_and_hold()
    return

def main():
    gpio_init()

    power_on()
    reset()

    ret = get_pled_state()
    if ret == 1:
        print("State: On")
    else:
        print("State: Off")

    # reset()
    # sleep(3)
    press()

    gpio_cleanup()

if __name__ == '__main__':
    main()
