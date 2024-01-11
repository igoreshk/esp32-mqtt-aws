

#!/usr/bin/env python3

"""GATT to MQTT"""

from __future__ import print_function

import sys

import ssl

import re

import time

import datetime

import logging, traceback

import paho.mqtt.client as mqtt

from bluepy import btle

IoT_protocol_name = "x-amzn-mqtt-ca"

aws_iot_endpoint = "endpoint.amazonaws.com"

url = "https://endpoint.amazonaws.com".format(aws_iot_endpoint)

ca = "path/Amazon-root-CA-1.pem"

cert = "path/crt/device.pem.crt"

private = "path/crt/private.pem.key"

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)

log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(log_format)

logger.addHandler(handler)

MQTT_TOPIC_BATTERY = 'serv'

MQTT_TOPIC_STATE = 'cons'

MQTT_PUBLISH_DELAY = 60

MQTT_CLIENT_ID = 'edge-01'

#MQTT_SERVER = 'edgeserver-01'

#MQTT_USER = 'username'

#MQTT_PASSWORD = 'pass'

DEIVCE_BTLE_ADDRESS = 'mac this bt device'

DEVICE_BATTERY_SERVICE_UUID = btle.UUID('180f')

DEVICE_BATTERY_CHARACTERISTIC_UUID = btle.UUID('2a19')

DEVICE_DATA_SERVICE_UUID = btle.UUID('4fafc201-1fb5-459e-8fcc-c5c9c331914b')

DEVICE_DATA_CHARACTERISTIC_UUID = btle.UUID('beb5483e-36e1-4688-b7f5-ea07361b26a8')

DEVICE_DATA_CHARACTERISTIC_HANDLE = 0x0010

BTLE_SUBSCRIBE_VALUE = bytes([0x01, 0x00])

BTLE_UNSUBSCRIBE_VALUE = bytes([0x00, 0x00])

battery = None

status = None

 

def on_connect(client, userdata, flags, rc):

    client.publish(MQTT_TOPIC_STATE, 'connected', 1, True)

 

class MyDelegate(btle.DefaultDelegate):

    def __init__(self):

        btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):

        fetch_sensor_data(bytearray(data).decode('utf-8'))

 

def ssl_alpn():

    try:

        #debug print opnessl version

        logger.info("open ssl version:{}".format(ssl.OPENSSL_VERSION))

        ssl_context = ssl.create_default_context()

        ssl_context.set_alpn_protocols([IoT_protocol_name])

        ssl_context.load_verify_locations(cafile=ca)

        ssl_context.load_cert_chain(certfile=cert, keyfile=private)

        return  ssl_context

    except Exception as e:

        print("exception ssl_alpn()")

        raise e

 

if __name__ == '__main__':

    topic = "topic_1"

    try:

        mqttc = mqtt.Client()

        ssl_context= ssl_alpn()

        mqttc.tls_set_context(context=ssl_context)

        logger.info("start connect")

        mqttc.connect(aws_iot_endpoint, port=8883)

        logger.info("connect success")

        mqttc.loop_start()

        while True:

            print('Connecting to ' + DEVICE_BTLE_ADDRESS)

            dev = btle.Peripheral(DEVICE_BTLE_ADDRESS)

            print('Set delegate')

            dev.setDelegate(MyDelegate())

            # Get battery level

            if battery is None:

                fetch_battery_level(dev)

                print('Battery level: ' + str(battery))

            # Subscribe to data characteristic

            if status is None:

                dev.writeCharacteristic(DEVICE_DATA_CHARACTERISTIC_HANDLE, BTLE_SUBSCRIBE_VALUE, True)

                while True:

                    if dev.waitForNotifications(1.0):

                        print('Open ' + status)

                        dev.writeCharacteristic(DEVICE_DATA_CHARACTERISTIC_HANDLE, BTLE_UNSUBSCRIBE_VALUE, True)

                        dev.disconnect()

                        break

               

            if battery is not None and status is not None:

                delay_gap = time.time() - last_msg_time

                if delay_gap < MQTT_PUBLISH_DELAY:

                    time.sleep(MQTT_PUBLISH_DELAY - delay_gap)

                publish_sensor_data(mqttc)

                last_msg_time = time.time()

                reset_variables()

    except Exception as e:

        logger.error("exception main()")

        logger.error("e obj:{}".format(vars(e)))

        logger.error("message:{}".format(e.message))

        traceback.print_exc(file=sys.stdout)

 

def reset_variables():

   global battery

    global status

    battery = None

    state = None

 

def fetch_battery_level(dev):

    global battery

    battery_service = dev.getServiceByUUID(DEVICE_BATTERY_SERVICE_UUID)

    battery_characteristic = battery_service.getCharacteristics(DEVICE_BATTERY_CHARACTERISTIC_UUID)[0]

    battery = ord(battery_characteristic.read())

 

def fetch_sensor_data(state):

    global status

    if match:

        status = match.group(1)

 

def publish_sensor_data(mqttc):

    mqttc.publish(MQTT_TOPIC_STATE, status, 1, True)

    mqttc.publish(MQTT_TOPIC_BATTERY, battery, 1, True)

 

if __name__ == '__main__':

    print('Starting GATT client')

    main()
