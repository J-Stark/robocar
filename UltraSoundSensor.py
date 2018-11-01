import time
import datetime
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.IN)


def reading(sensor):
    pingtime = 0
    echotime = 0
    if sensor == 0:
        print("Working")
        GPIO.output(15,GPIO.LOW)
        GPIO.output(15,GPIO.HIGH)
        pingtime=time.time()
        time.sleep(0.00001)
        GPIO.output(15,GPIO.LOW)
        GPIO.output(15,GPIO.HIGH)
        pingtime=time.time()
        time.sleep(0.00001)
        GPIO.output(15,GPIO.LOW)
        while GPIO.input(16)==0:
            pingtime = time.time()
        while GPIO.input(16)==1:
            echotime=time.time()
        if (echotime is not None) and (pingtime is not None):
            elapsedtime = echotime - pingtime
            distance = elapsedtime * 17000
        else:
            distance = 0
        return distance

while True:
    range = reading(0)
    print("Range is " + str(range))
    time.sleep(0.0000000000000000001)

