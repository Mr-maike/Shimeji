#Código Base para Teste com o Sensor DHT11 com o Microcontrolador Raspberry Pi 4

#Carregar as bibliotecas (Consultar README)
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

#Definir o tipo de sensor que será trabalhado
sensor = Adafruit_DHT.DHT11

GPIO.setmode(GPIO.BOARD)

#Define a GPIO do Pino conectado ao Sensor
pino_sensor = 25

print("*** Valores de Temperatura e Umidade")

while 1:
    umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor)

    if umid is not None and temp is not None:
        print("Temperatura = {0:0.1f} Umidade = {1:0.1f}n".format(temp, umid))
        print("Aguardar 1.5s para a proxima leitura...")
        time.sleep(1.5)

    else:
        print("Falha ao Ler os dados do DHT11")

