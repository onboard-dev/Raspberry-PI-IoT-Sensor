#onboard IoT board
# Capacitive Soil Moisture Sensor v1.2 
# AliExpress https://bit.ly/3dMIDjD
from gpiozero import MCP3004,LED
from time import sleep

Vref = 3.3

adc = MCP3004(channel=0,device=1)
SensorPower0=LED(20)
SensorPower0.on()

while True:
	SensorPower0.on()
	print(adc.value*1000)
	SensorPower0.off()
	sleep(0.2)
