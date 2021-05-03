import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Green LED
GPIO.setup(21, GPIO.OUT)
# Yellow LED
GPIO.setup(20, GPIO.OUT)
# Red LED :)
GPIO.setup(16, GPIO.OUT)

# Button :/
GPIO.setup(2, GPIO.IN)

print('Program running')

while True:
    if not GPIO.input(2):
        print('pushed')
        GPIO.output(16, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(20, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        time.sleep(5)
        GPIO.output(21, GPIO.LOW)
        GPIO.output(20, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(20, GPIO.LOW)
    else:
        GPIO.output(16, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(16, GPIO.LOW)
        time.sleep(0.05)

GPIO.cleanup()