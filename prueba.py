import RPi.GPIO as GPIO
import time
import adafruit_dht


ESPERA = 0.5
PIN = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

sensor = adafruit_dht.DHT22(16)
while True:
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(ESPERA)
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(ESPERA)
    try:
        humedad = sensor.humidity
        temperatura = sensor.temperature

        if humedad is not None and temperatura is not None:
            print("DHT Sensor - Temperatura: ",str(temperatura))
            print("DHT Sensor - Humedad: ",str(humedad))
        else:
            print('Error al obtener la lectura del sensor')
    except:
        pass