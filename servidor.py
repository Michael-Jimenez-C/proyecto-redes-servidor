from flask import Flask, jsonify
import Adafruit_DHT
import struct, os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
sensor = Adafruit_DHT.DHT11

app=Flask(__name__)

@app.route("/")
def main():
    R= Adafruit_DHT.read_retry(sensor,23)
    h=R[0]
    t=R[1]
    if h is not None and t is not None:
        print('values',R)
        return jsonify({'temperatura':t,'humedad':h}) 
    print('Failed to read sensor data')
    return jsonify({'error':'can\'t read'})

@app.route("/encriptado")
def enc():
    R= Adafruit_DHT.read_retry(sensor,23)
    h=R[0]
    t=R[1]
    if h is not None and t is not None:
        print('values',R)
        datos={'temperatura':t,'humedad':h}
        nonce = b'o\x11\x0ef\x00\xf9\xd9\n'
        key = b'\x83%\xc9L/\xbd\x05\xdcv"\x99\x92\xa4vl\xb0\xbfYQ\x88\x13j\xccQ}Qvi4\x08\x88\x15'
        counter = 0
        full_nonce = struct.pack("<Q", counter) + nonce
        algorithm = algorithms.ChaCha20(key, full_nonce)
        cipher = Cipher(algorithm, mode=None)
        encryptor = cipher.encryptor()
        ct = encryptor.update(bytes(str(datos),'utf-8'))
        k=ct.decode('latin-1')
        return k
    print('Failed to read sensor data')
    return jsonify({'error':'can\'t read'})


app.run(host="0.0.0.0")