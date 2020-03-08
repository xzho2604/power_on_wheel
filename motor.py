import RPi.GPIO as gpio
import time

def init_motor():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

def init_wheel():
    gpio.setmode(gpio.BCM)
    # direction motor
    gpio.setup(13, gpio.OUT)
    gpio.setup(26, gpio.OUT)

def forward(sec):
    init_motor()
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)
    #time.sleep(sec)
    #gpio.cleanup() # stop

def turn(sec):
    init_wheel()
    gpio.output(13, True)
    gpio.output(26, False)
    time.sleep(sec)
    gpio.cleanup() # stop


def reverse(sec):
    init_motor()
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(sec)
    gpio.cleanup()

    print("forward")
    forward(4)
    print("reverse")
    reverse(2)

forward(1)
turn(1)




