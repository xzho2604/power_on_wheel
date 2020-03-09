import RPi.GPIO as gpio
import time

def init_motor():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)

def init_wheel():
    gpio.setmode(gpio.BCM)
    # direction motor
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

def forward():
    init_motor()
    gpio.output(17, True)
    gpio.output(22, False)
    #time.sleep(sec)
    #gpio.cleanup() # stop

def stop_motor():
    init_motor()
    gpio.output(17, False)
    gpio.output(22, False)

def stop_wheel():
    init_wheel()
    gpio.output(23, False)
    gpio.output(24, False)

def turn_right():
    init_wheel()
    gpio.output(23, False)
    gpio.output(24, True)

def turn_left():
    init_wheel()
    gpio.output(23, True)
    gpio.output(24, False)

def reverse():
    init_motor()
    gpio.output(17, False)
    gpio.output(22, True)

#forward(1)




