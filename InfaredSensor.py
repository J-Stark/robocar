# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
IRsensor1 = 7 # Broadcom pin

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(IRsensor1, GPIO.IN) # The sensor set as input 

# The infinite loop that will constatly print what the sensor detects
while True:
        A = GPIO.input(IRsensor1)
        print (A)
        time.sleep(0.01)

