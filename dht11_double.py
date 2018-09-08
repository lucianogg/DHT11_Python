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
    result1 = instance1.read()
    result2 = instance2.read()
    if result1.is_valid() and result2.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C and %d C" % (result1.temperature,result2.temperature))
        print("Humidity: %d %% and %d %%" % (result1.humidity, result2.humidity))
    time.sleep(10)
