#!/usr/bin/env python
#-*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import sys
from time import sleep

mqtt_broker="example.com"
#mqtt_broker="iot.eclipse.org"
identity="CHANGE_ME"

def main():
    client = mqtt.Client()
    try:
        client.connect(mqtt_broker, 1883, 60)
        client.publish("/iot_pmc/"+identity+"/control",'{"power":"press"}' )
        sleep(1)
        client.publish("/iot_pmc/"+identity+"/control",'{"power":"press_and_hold"}' )
        sleep(1)
        client.publish("/iot_pmc/"+identity+"/control",'{"power":"cold_boot"}' )
        sleep(1)
        client.publish("/iot_pmc/"+identity+"/control",'{"power":"reset"}' )
        sleep(1)
        client.publish("/iot_pmc/"+identity+"/control",'{"power":"power_on"}' )
        sleep(1)
        client.publish("/iot_pmc/"+identity+"/control",'{"power":"power_off"}' )
        sleep(1)
        client.disconnect()
    except KeyboardInterrupt:
        client.disconnect()
        sys.exit()

if __name__ == "__main__":
    main()
