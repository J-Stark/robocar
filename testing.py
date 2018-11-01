import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
# The GPIO Pins can be changed here
# The pins for the right side motors
GPIO.setup(13,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
# The pins for the left side motors
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
# The PWM
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
R=GPIO.PWM(11,50)
L=GPIO.PWM(12,50)
R.start(0)
L.start(0)
f=open("/var/www/html/testing.txt", "r")
# The loop where speed and the way the motors spin can be tuned
while True:
	time.sleep(0.6)
	contents = f.read()
	if(contents=='2\n'):
	  GPIO.output(13,GPIO.LOW)
	  GPIO.output(8,GPIO.HIGH)
	  GPIO.output(15,GPIO.LOW)
	  GPIO.output(16,GPIO.HIGH)
	  R.ChangeDutyCycle(100)
	  L.ChangeDutyCycle(100)
	  print("Fast Forward")
	elif(contents=='1\n'):
          GPIO.output(13,GPIO.LOW)
          GPIO.output(8,GPIO.HIGH)
          GPIO.output(15,GPIO.LOW)
          GPIO.output(16,GPIO.HIGH)
          R.ChangeDutyCycle(50)
          L.ChangeDutyCycle(50)
	  print("Forward")
	elif(contents=='-2\n'):
          GPIO.output(13,GPIO.HIGH)
          GPIO.output(8,GPIO.LOW)
          GPIO.output(15,GPIO.HIGH)
          GPIO.output(16,GPIO.LOW)
          R.ChangeDutyCycle(100)
          L.ChangeDutyCycle(100)
	  print("Fast Backwards")
	elif(contents=='-1\n'):
          GPIO.output(13,GPIO.HIGH)
          GPIO.output(8,GPIO.LOW)
          GPIO.output(15,GPIO.HIGH)
          GPIO.output(16,GPIO.LOW)
          R.ChangeDutyCycle(50)
          L.ChangeDutyCycle(50)
	  print("Backwards")
	elif(contents=="0\n"):
	  R.ChangeDutyCycle(0)
	  L.ChangeDutyCycle(0)
	  print("Stopped")
	elif(contents=="L\n"):
          GPIO.output(13,GPIO.LOW)
          GPIO.output(8,GPIO.HIGH)
          GPIO.output(15,GPIO.LOW)
          GPIO.output(16,GPIO.HIGH)
          R.ChangeDutyCycle(25)
          L.ChangeDutyCycle(0)
	  print("Left")
	elif(contents=="R\n"):
          GPIO.output(13,GPIO.LOW)
          GPIO.output(8,GPIO.HIGH)
          GPIO.output(15,GPIO.LOW)
          GPIO.output(16,GPIO.HIGH)
          R.ChangeDutyCycle(0)
          L.ChangeDutyCycle(25)
	  print("Right")
	print(contents)
	f.seek(0.0)
GPIO.cleanup()
