import RPi.GPIO as GPIO
import time

ESPERA = 0.5
PIN = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)
while True:
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(ESPERA)
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(ESPERA)