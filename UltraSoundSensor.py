import RPi.GPIO as GPIO
import time
import signal
import sys
import atexit

# Setup mode
GPIO.setmode(GPIO.BOARD)

# GPIO Pins for sensors
IRsensor1 = 35
IRsensor2 = 36
pinTrigger = 38
pinEcho = 37

# Right side motors
GPIO.setup(13,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)

# Left side motors
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

# PWM
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
R = GPIO.PWM(11,50)
L = GPIO.PWM(12,50)

# Sensors
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)
GPIO.setup(IRsensor1, GPIO.IN)
GPIO.setup(IRsensor2, GPIO.IN)

# Starting the car with reasonable speed
GPIO.output(13,GPIO.LOW)
GPIO.output(8,GPIO.HIGH)
GPIO.output(15,GPIO.LOW)
GPIO.output(16,GPIO.HIGH)


#Start of the motors
R.start(0)
L.start(0)

# When Exiting The Program
def close(signal, frame):
	print("\nTurning off ultrasonic distance detection...\n")
	GPIO.cleanup()
	sys.exit(0)
def Stop():
	R.ChangeDutyCylce(0)
	L.ChangeDutyCycle(0)

signal.signal(signal.SIGINT, close)
atexit.register(Stop)

while True:
	#Infared
	A = GPIO.input(IRsensor1)
	B = GPIO.input(IRsensor2)

	# sets a pulse that is done by setting the trigger to high then after a nano second setting to low
	GPIO.output(pinTrigger, True)
	time.sleep(0.00001)
	GPIO.output(pinTrigger, False)

	startTime = time.time()
	stopTime = time.time()

	# Saving here the start time
	while 0 == GPIO.input(pinEcho):
		startTime = time.time()

	# Saving time of arrival
	while 1 == GPIO.input(pinEcho):
		stopTime = time.time()

	#  the time difference between start and arrival

	TimeElapsed = stopTime - startTime
	# multiply with the sonic speed (34300 cm/s)
	# and divide by 2, because there and back

	distance = (TimeElapsed * 34300) / 2

	# The Conditions of the moving parts
	if distance <= 90 and A==0 and B==0:
		GPIO.output(13,GPIO.LOW)
		GPIO.output(8,GPIO.HIGH)
		GPIO.output(15,GPIO.LOW)
		GPIO.output(16,GPIO.HIGH)
		R.ChangeDutyCycle(45)
		L.ChangeDutyCycle(45)
	elif A == 1 or B == 1:
		R.ChangeDutyCycle(0)
		L.ChangeDutyCycle(0)
		time.sleep(0.01)
		GPIO.output(13,GPIO.HIGH)
		GPIO.output(8,GPIO.LOW)
		GPIO.output(15,GPIO.HIGH)
		GPIO.output(16,GPIO.LOW)
		R.ChangeDutyCycle(50)
		L.ChangeDutyCycle(50)
		time.sleep(0.9)
		GPIO.output(13,GPIO.LOW)
		GPIO.output(8,GPIO.HIGH)
		GPIO.output(15,GPIO.LOW)
		GPIO.output(16,GPIO.HIGH)
		R.ChangeDutyCycle(35)
		L.ChangeDutyCycle(0)
		time.sleep(0.9)
	else:
		GPIO.output(8,GPIO.HIGH)
		GPIO.output(13,GPIO.LOW)
		GPIO.output(15,GPIO.LOW)
		GPIO.output(16,GPIO.HIGH)
		R.ChangeDutyCycle(35)
		L.ChangeDutyCycle(0)
		if distance <= 90 and A== 0 and B==0:
			break
		time.sleep(0.9)

	# the format which makes the given to us number into a cm
	print ("Distance: %.1f cm" % distance)
