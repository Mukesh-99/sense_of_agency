"""
send_UDP_tester.py
Tests "socket_recv_test.py by sending list of ints as bytes to socket for BrainGate drone simulation
Author: Derek Wacks
"""

import struct
import numpy as np
import time
from socket import (
    socket,
    timeout as sockettimeoutexception,
    AF_INET,
    SOCK_DGRAM,
    SOL_SOCKET,
    SO_RCVBUF,
    SO_REUSEADDR,
)

#host = "127.0.0.1"   # local host IP
#udpPort = 8667       # one of my top 9999 favorite port numbers
#host = "192.168.30.100" # T11 personal comp staticly set
udpPort = 26504
host = "192.168.30.3" # PC2 staticly set
#udpPort = 26504

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
packet_delay = 0.02  # delay between sending packets

def waiting(length):
    """
    delay function
    """
    print("waiting for ", length," seconds")
    time.sleep(length)

def take_off_or_land():
    """
    take off or land, depending on drone's current state
    (controlled with discreteAction=1.0)
    """
    packetID = float(0)
    timeStamp = float(0.0)
    x = float(0)
    y = float(0)
    discreteAction = float(1.0)
    commandCounter = float(0)
    packet = np.array([packetID, timeStamp, x, y, discreteAction, commandCounter])
    b = packet.tobytes()
    s.sendto(b, (host, udpPort))
    time.sleep(packet_delay)
    return


def go_up_or_down(length, dir, discrete_action):
    """
    param: length, number of packets to send with this command
    param: dir, "up" or "down" string for print statement
    param: discrete_action, 4.0 or 5.0 discrete gesture to go up(-)/down(+)
    if discrete_action = 4, go up
    if discrete_action = 5, go down
    """
    print("going "+str(dir)+" with "+str(length)+" gestures")
    for i in range(length):
        packetID = float(i)
        timeStamp = float(0.0)
        x = float(0)
        y = float(0)
        discreteAction = float(discrete_action)
        commandCounter = float(i)
        packet = np.array([packetID, timeStamp, x, y, discreteAction, commandCounter])
        b = packet.tobytes()
        s.sendto(b, (host, udpPort))
        time.sleep(packet_delay)  # time between when packets are sent with discrete gestures
        # Note: this time could 20ms (real packet delay) but each command is overwritten
    return

def move(length, x_val, y_val):
    """
    param: length, number of packets to send with this command
    param: x_val, x for 2D "cursor" control (used for yaw left/right)
    param: y_val, y for 2D "cursor" control (used for forward/backward velocity)
    """
    for i in range(length):
        packetID = float(i)
        timeStamp = float(0.0)
        x = float(x_val)
        y = float(y_val)
        discreteAction = float(0.0)
        commandCounter = float(i)
        packet = np.array([packetID, timeStamp, x, y, discreteAction, commandCounter])
        b = packet.tobytes()
        s.sendto(b, (host, udpPort))
        time.sleep(packet_delay)
    return

def change_gain(gesture):
    """
    param: gesture = discrete_action,
    change gain with discrete action
    if 2.0, gain+=0.1
    if 4.0, gain-=0.1
    """
    if gesture==2.0:
        print("Increasing gain")
    elif gesture==4.0:
        print("Decreasing gain")
    packetID = float(0)
    timeStamp = float(0.0)
    x = float(0)
    y = float(0)
    discreteAction = float(gesture)
    commandCounter = float(0)
    packet = np.array([packetID, timeStamp, x, y, discreteAction, commandCounter])
    b = packet.tobytes()
    s.sendto(b, (host, udpPort))
    time.sleep(packet_delay)
    return


def new_log():
    """
    increment COUNTER and change log file in drone_control_from_UDP.py to drone_exp_COUNTER.log
    (controlled with discreteAction=91.0)
    """
    packetID = float(0)
    timeStamp = float(0.0)
    x = float(0)
    y = float(0)
    discreteAction = float(90.0)
    commandCounter = float(0)
    packet = np.array([packetID, timeStamp, x, y, discreteAction, commandCounter])
    b = packet.tobytes()
    s.sendto(b, (host, udpPort))
    return

def next_experiment():
    """
    increment COUNTER and change log file in drone_control_from_UDP.py to drone_exp_COUNTER.log
    (controlled with discreteAction=91.0)
    """
    packetID = float(0)
    timeStamp = float(0.0)
    x = float(0)
    y = float(0)
    discreteAction = float(93.0)
    commandCounter = float(0)
    packet = np.array([packetID, timeStamp, x, y, discreteAction, commandCounter])
    b = packet.tobytes()
    s.sendto(b, (host, udpPort))
    return


def soft_reset():
    """
    Not a real command, used for meta control to reset simulation
    """
    print("resetting")
    packetID = float(0)
    timeStamp = float(0.0)
    x = float(0)
    y = float(0)
    discreteAction = float(91.0)  # RESETTING
    commandCounter = float(0)
    packet = np.array([packetID, timeStamp, x, y, discreteAction, commandCounter])
    b = packet.tobytes()
    s.sendto(b, (host, udpPort))
    return

def hard_reset():
    """
    Not a real command, used for meta control to reset simulation
    """
    print("resetting")
    packetID = float(0)
    timeStamp = float(0.0)
    x = float(0)
    y = float(0)
    discreteAction = float(92.0)  # RESETTING
    commandCounter = float(0)
    packet = np.array([packetID, timeStamp, x, y, discreteAction, commandCounter])
    b = packet.tobytes()
    s.sendto(b, (host, udpPort))

    waiting(1)
    exit()


def move_full(length, x_val, y_val, discrete_action):
    """
    param: length, number of packets to send with this command
    param: x_val, x for 2D "cursor" control (used for yaw left/right)
    param: y_val, y for 2D "cursor" control (used for forward/backward velocity)
    """
    for i in range(length):
        packetID = float(i)
        timeStamp = float(0.0)
        x = float(x_val)
        y = float(y_val)
        commandCounter = float(i)
        packet = np.array([packetID, timeStamp, x, y, discrete_action, commandCounter])
        b = packet.tobytes()
        s.sendto(b, (host, udpPort))

        discrete_action = 0  # resetting discrete gesture

        time.sleep(packet_delay)

    return


def exp_1():
    print("Take off")
    take_off_or_land()
    print("Go up")
    move_full(length=200, x_val=0, y_val=0, discrete_action=5.0)


def exp_2():
    print("Take off")
    take_off_or_land()
    print("Go up")
    move_full(length=200, x_val=0, y_val=0, discrete_action=5.0)
    print("Go down")
    move_full(length=200, x_val=0, y_val=0, discrete_action=4.0)

def exp_3():
    print("Take off")
    take_off_or_land()
    print("Go up")
    move_full(length=200, x_val=0, y_val=0, discrete_action=5.0)
    print("Go forwards")
    move_full(length=200, x_val=0, y_val=0.005, discrete_action=0.0)
    print("Go backwards")
    move_full(length=200, x_val=0, y_val=-0.005, discrete_action=0.0)

def exp_4():
    print("Take off")
    take_off_or_land()
    print("Go up")
    move_full(length=200, x_val=0, y_val=0, discrete_action=5.0)
    print("Rotate left")
    move_full(length=200, x_val=-0.005, y_val=0, discrete_action=0.0)
    print("Rotate right")
    move_full(length=200, x_val=0.005, y_val=0, discrete_action=0.0)
    #print("Land")
    #take_off_or_land()

def exp_5():
    print("Take off (intended for gear_knob mode)")
    take_off_or_land()
    print("Go up")
    move_full(length=200, x_val=0, y_val=0, discrete_action=5.0)
    print("Gear forwards")
    move_full(length=1, x_val=-0.005, y_val=0, discrete_action=2.0)
    print("Move forwards")
    move_full(length=200, x_val=0, y_val=0.007, discrete_action=0.0)
    print("Gear neutral")
    move_full(length=1, x_val=-0.005, y_val=0, discrete_action=3.0)
    print("Gear reverse")
    move_full(length=1, x_val=-0.005, y_val=0, discrete_action=3.0)
    print("Move backwards")
    move_full(length=200, x_val=0, y_val=-0.007, discrete_action=0.0)

############
#   Tests  #
############
def tests():
    print("taking off...")
    take_off_or_land()
    """
    go_up_or_down(length=1, dir="up", discrete_action=4.0)
    waiting(3)  # delay between user sending discrete gestures
    go_up_or_down(length=1, dir="up", discrete_action=4.0)
    waiting(1)

    print("going forwards")
    move(length=100, x_val=0, y_val=1)

    print("going right")
    move(length=100, x_val=0.6, y_val=0)

    #for i in range(20):
    #    change_gain(gesture=2.0)
    """
   # move_full(length=200, x_val=0, y_val=0.5, discrete_action=0.0)
    print("up")
    move_full(length=200, x_val=0, y_val=0, discrete_action=5.0)  # go up
    print("up and forward")
    move_full(length=200, x_val=0, y_val=0.005, discrete_action=5.0) # go up and forward?
    print("down")
    move_full(length=200, x_val=0, y_val=0.0, discrete_action=4.0)
    print("backward")
    move_full(length=200, x_val=0, y_val=-0.005, discrete_action=0)

    #print("going forwards")
    #move(length=200, x_val=0, y_val=1)

    #print("going forwards and left")
    #move(length=150, x_val=-0.3, y_val=1)

    #print("going forwards and right")
    #move(length=150, x_val=0.3, y_val=1)

    #print("going backwards")
    #move(length=150, x_val=0, y_val=-5)

# Run all tests
#tests()
# Reset simulation
#reset()


def full_test():
    print("pre-test packets (nothing should happen)")
    move_full(length=200, x_val=0, y_val=0, discrete_action=0.0)
    print("taking off...")
    take_off_or_land()
    print("up")
    move_full(length=200, x_val=0, y_val=0, discrete_action=5.0)
    print("up and forward")
    move_full(length=200, x_val=0, y_val=0.005, discrete_action=5.0)
    print("forward")
    move_full(length=1000, x_val=0, y_val=0.005, discrete_action=0.0)


def vel_test():
    print("taking off...")
    take_off_or_land()
    print("up")
    move_full(length=200, x_val=0, y_val=0, discrete_action=5.0)
    print("forward y=0.005")
    move_full(length=150, x_val=0, y_val=0.005, discrete_action=0.0)
    print("forward y=0.007")
    move_full(length=150, x_val=0, y_val=0.007, discrete_action=0.0)
    print("forward y=0.01")
    move_full(length=150, x_val=0, y_val=0.01, discrete_action=0.0)
    print("forward y=0.02")
    move_full(length=150, x_val=0, y_val=0.02, discrete_action=0.0)





if __name__ == '__main__':
    while True:
        val = input("Enter control choice (0: new log,   1: reset,   2: QUIT,   3: new log and reset,   4-9: tests):\n")
        if val == str(0):
            new_log()
        if val == str(1):
            soft_reset()
        if val == str(2):
            hard_reset()
        if val == str(3):
            next_experiment()
        if val == str(4):
            tests()
        if val == str(5):
            exp_1()
        if val == str(6):
            exp_2()
        if val == str(7):
            exp_3()
        if val == str(8):
            exp_4()
        if val == str(9):
            exp_5()
        if val == "ft":
            full_test()
        if val == "v":
            vel_test()

