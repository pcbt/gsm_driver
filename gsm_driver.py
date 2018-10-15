import commands
import RPi.GPIO as GPIO
import time, threading
import paho.mqtt.client as mqtt


client = mqtt.Client()

def on_message(client, userdata, message):
    print str(message.payload.decode("utf-8"))
    if message.payload.decode("utf-8") == "0":
	print "grasd"
	#light_off()
    if message.payload.decode("utf-8") == "1":
	#light_on()
	print "asdwasww"



def light_on():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.OUT)
    GPIO.output(37, False)



def light_off():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.OUT)
    GPIO.output(37, True)

def power_up():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(1, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, True)
    GPIO.output(1, True)
    GPIO.output(6, False)
    time.sleep(3)
    GPIO.output(6, True)
    GPIO.cleanup()

def start_module():
    power_up()
    ppp = commands.getstatusoutput('sudo pon AirNet')


def control_module():
    cmd = commands.getstatusoutput('ifconfig ppp0')
    if cmd[0] != 0:
	print "Sorun"
	client.loop_stop()
        start_module()
        time.sleep(30)
        control_module()
	print "Sorun duzeltildi"
	return 1
    else:
	return 0

def periodic_control():
    if control_module():
	client.connect("testserver.airchip.com.tr")
	print client.subscribe("AirCity/Tokat", qos = 1)
	client.on_message = on_message
	client.publish("test2", "Connected")
        client.loop_start()
    threading.Timer(60,periodic_control).start()
    print "Kontrol"


commands.getstatusoutput('sudo poff AirNet')
periodic_control()
