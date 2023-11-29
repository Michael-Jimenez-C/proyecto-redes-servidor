import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
humedad, temperatura = Adafruit_DHT.read(sensor,27)