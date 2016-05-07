#!/usr/bin/python
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import json
from time import sleep

mqtt_broker="example.com"
#mqtt_broker="iot.eclipse.org"
identity="CHANGE_ME"

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

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/iot_pmc/"+identity+"/control")
    return

def on_message(client, userdata, msg):
    value = json.loads(msg.payload)
    request = value.get('power')

    print "request: {0}".format(request)

    if request == "press":
        press()
    elif request == "press_and_hold":
        press_and_hold()
    elif request == "cold_boot":
        cold_boot()
    elif request == "reset":
        reset()
    elif request == "power_on":
        power_on()
    elif request == "power_off":
        power_off()
    return


    return

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

    last_pled_state=0

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(mqtt_broker, 1883, 300)
        client.loop_start()
        while True:
            ret = get_pled_state()
            if last_pled_state != ret:
                last_pled_state = ret
                if ret == 0:
                    client.publish("/iot_pmc/"+identity+"/power_state",'{"state":"off"}' )
                elif ret == 1:
                    client.publish("/iot_pmc/"+identity+"/power_state",'{"state":"on"}' )
            sleep(5)
    except KeyboardInterrupt:
        print "exit"
        client.loop_stop()
        gpio_cleanup()

if __name__ == "__main__":
    main()
