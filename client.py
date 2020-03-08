"""
change the pip install pyPS4Controller modeul in:
/usr/local/lib/python3.5/dist-packages/pyPS4Controller

controller interface:
-----------------------
on_R3_right: left to right range: [-32767,32767]
on_L2_press: pressing down range: [-32431 ,32767]
             depend on the releasing speed the lower can be
             -20945 one fast release

controller protocol:
-----------------------

Motor and servo control:
-----------------------
max pulxe lenght of 4096
- servo control
    pwm.set_pwm(1,0,servo_mid)
- Motor control
    pwm.set_pwm(1,0,servo_forward)

"""


import socket
import json

#import RPI.GPIO as GPIO
import time
#import Adafruit_PCA9685


# set up the initial connection with the host using udp
def udpInit(host,port):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to the port
    server_address = (host, port)
    sock.bind(server_address)
    print("server bind to: " ,host , port)

    '''
    #----------------------------------------
    # send initial shaske message for client to get the
    # server address for communication
    message="server init handshake!"
    sock.sendto(message.encode(),("203.194.11.102",8888))
    print("sent server init handshake")

    #----------------------------------------
    '''

    return sock


# given the data received from the socket parse the right command
def parseCmd(data):
    if("on_L2_press" in data): # goingforward
       motorForward(data["on_L2_press"])
       #motorControl(motor_forward)
    if("on_L2_release" in data): # motor stop
       #motorControl(data["on_L2_press"])
       motorControl(motor_stop)
    if("on_down_arrow_press" in data): # motor back
       #motorControl(data["on_L2_press"])
       motorControl(motor_back)
       #print("pressed down!!!!")
    if("on_down_arrow_release" in data): # motor back
       #motorControl(data["on_L2_press"])
       motorControl(motor_stop)
       #print("released down!!!!")
    if("on_R3_left" in data): # turn left
       servoTurn(data["on_R3_left"])
       #servoControl(servo_left)
    if("on_R3_right" in data): # turn right
       servoTurn(data["on_R3_right"])
       #servoControl(servo_right)
    if("on_R3_rest" in data): # server center
       #servoControl(servo_stop)
       servoControl(servo_mid)

from motor import *
def process_cmd(data):
    if("on_up_arrow_press" in data):
        forward()
    if("on_up_arrow_release" in data):
        stop_motor()
    if("on_down_arrow_press" in data): # motor back
        reverse()
    if("on_down_arrow_release" in data): # motor back
        stop_motor()

    if("on_x_press" in data): # motor back
        turn_right()
    if("on_x_release" in data): # motor back
        stop_wheel()
    if("on_triangle_press" in data): # motor back
        turn_left()
    if("on_triangle_release" in data): # motor back
        stop_wheel()
# ----------------------------------------------
# init message send to the NAT server
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s = udpInit("",5200)

# UDP receive data
while True:
    data, address = s.recvfrom(4096)
    #data = conn.recv(4096)
    if(data):
        data = data.decode()
        # in case of dupicate server message sent , so that ack will
        # be received twice
        print("received data:",data)
        try:
            data = json.loads(data)
        except:
            continue

        process_cmd(data)







