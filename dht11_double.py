import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance1 = dht11.DHT11(pin=17)
instance2 = dht11.DHT11(pin=27)

while True:
    result = instance1.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Temperature: %d F" % ((result.temperature * 9/5)+32))
        print("Humidity: %d %%" % result.humidity)
    result = instance2.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Temperature: %d F" % ((result.temperature * 9/5)+32))
        print("Humidity: %d %%" % result.humidity)

    time.sleep(1)
