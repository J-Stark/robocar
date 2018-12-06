# External module imports
import RPi.GPIO as GPIO
import time
import atexit

# Pin Definitons:
# Sensor
IRsensor1 = 35 # pin
IRsensor2 = 36 # pin
#IRsensor3 = 37 # pin
# Pin Setup:
GPIO.setmode(GPIO.BOARD) # BOARD pin-numbering scheme
# Right side motors
GPIO.setup(13,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
# Left side motors
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
# PWM
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
R=GPIO.PWM(11,50)
L=GPIO.PWM(12,50)
# Sensors
GPIO.setup(IRsensor1, GPIO.IN) # The sensor set as input
GPIO.setup(IRsensor2, GPIO.IN)
#GPIO.setup(IRsensor3, GPIO.IN)
# Starting the car with reasonable speed
GPIO.output(13,GPIO.LOW)
GPIO.output(8,GPIO.HIGH)
GPIO.output(15,GPIO.LOW)
GPIO.output(16,GPIO.HIGH)
# Further setup for sensors
A = GPIO.input(IRsensor1)
B = GPIO.input(IRsensor2)
# C = GPIO.input(IRsensor3)
#Start of the motors
R.start(0)
L.start(0)

def StopCar():
	R.ChangeDutyCycle(0)
	L.ChangeDutyCycle(0)
	GPIO.cleanup()
# The infinite loop that will constatly print what the sensor detects
while True:
	A = GPIO.input(IRsensor1)
	B = GPIO.input(IRsensor2)
	if A == 1 and B == 0:
		R.ChangeDutyCycle(0)
		L.ChangeDutyCycle(55)
		time.sleep(0.01)
	elif B == 1 and A == 0:
		L.ChangeDutyCycle(0)
		R.ChangeDutyCycle(55)
		time.sleep(0.01)
	elif A == 0 and  B == 0:
		R.ChangeDutyCycle(30)
		L.ChangeDutyCycle(30)
	elif A == 1 and B == 1:
		R.ChangeDutyCycle(30)
		L.ChangeDutyCycle(30)
	print ("Sensors:",A,B)

atexit.register(StopCar)
