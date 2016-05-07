# iot-pmc-core
IoT Power Management Controller (core module)

## Setup
- for Fedora ARM or Pidora

    $ sudo yum install python-rpi-gpio

    $ sudo yum install python-paho-mqtt

- for RaspbianOS

    $ sudo apt install python-pip python-rpi.gpio

    $ sudo pip install paho-mqtt

## Usage
1. Build your MQTT broker.
 - If you want to build by ansible. see also build_activemq_broker.yml
2. Modify mqtt_broker value in source code.
3. Connect PMC daughter board on GPIO of your RasPi.
4. Execute iot_pmc_subscriber.py on your RasPi.

    $ python ./iot_pmc_subscriber.py

## for testing
And so if you want to test about MQTT publisher. Please execute following command on another terminal.

    $ python ./iot_pmc_publisher_test.py

