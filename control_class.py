"""
control.py
Receives UDP packets from a socket
Author: Derek Wacks
"""
# Imports
import time
import sys
import math
import numpy as np
from udp_socket_helper import BGUDPSocket
from neural_command import NeuralCommand
import asyncio
import logging


class ControlFacilitator:
    """
    Class to handle UDP communication between the BrainGate Real-Time Model
    and research session experiments built in Python.

    Facilitate UDP packet receiving and game state logging (sending back to RTM)
    """
    def __init__(
        self,
        local_log_dir=None,
        testing_bool=None,

    ):


        self.log_dir_loc = local_log_dir

        ####################
        # Initial log file #
        ####################
        if local_log_dir is None:
            curr_t = time.asctime().replace(" ", "_").replace(":", "_")
            log_dir_loc = '../../Data/GameData/CURRENTLOG/'
        fname = log_dir_loc + curr_t + '_exp_0.log'  # writes to Data/ (outside of research-sessions)
        logging.basicConfig(filename=fname, level=logging.DEBUG)
        header = ",t,x,y,dis,vz,x_pos,y_pos,z_pos,x_v,y_v,z_v"  # adding header to view log file as csv
        logging.info(header)

###############
# IP and port #
###############
# Test settings for locally sending commands as packets
testing_bool = True
if testing_bool:
    udpRecvPort = 26504 # originally testing on 8667
    UDPHostName_Address = "192.168.30.3"  # PC2 (staticly set)
    loc = "192.168.30.1" # Python scripts running on PC1
    #UDPHostName_Address = "127.0.0.1"
else:
    udpRecvPort = 26504
    UDPHostName_Address = "192.168.30.100"  # T11 personal comp staticly set FOR R_SESSION
    loc = "192.168.30.3" # Python scripts running on PC2

############################
# IP/port for RTM feedback #
############################
udpSendOnlyPort = 26400  # "Send from" port
rtmUdpPort = 26400  # Send feedback to real time model at this IP
rtmUdpHost = "192.168.30.4"


#############
#   Params  #
#############
start_time = time.time()  # in-game start time


def change_logger():
    global experiment_counter
    experiment_counter += 1
    log = logging.getLogger()  # root logger
    for hdlr in log.handlers[:]:  # remove all old handlers
        log.removeHandler(hdlr)
    curr_t = time.asctime().replace(" ", "_").replace(":", "_")
    name = log_dir_loc + curr_t + '_exp_' + str(experiment_counter) + '.log' # writes to Data/
    logging.basicConfig(filename=name, level=logging.DEBUG)
    header = ",t,x,y,dis,vz,x_pos,y_pos,z_pos,x_v,y_v,z_v"
    logging.info(header)
    print("Log name CHANGED:", name)


def interact(udpPacket):
    """
    Parse packet!
    :param udpPacket
    """
    neuralCommand = NeuralCommand.fromBytes(udpPacket)  # Get neural command from UDP packet
    commandCounter = neuralCommand.commandCounter
    nspTstamp = neuralCommand.nspTimestamp
    discrete_click = neuralCommand.discreteAction  # 0-6 incl.
    x = neuralCommand.x
    y = neuralCommand.y

    actions = [x, y, discrete_click]

    if discrete_click == 1.0:
        # TODO: add keyboard control
        pass
    elif discrete_click == 2.0:
        # TODO: add keyboard control
        pass
    elif discrete_click == 92.0:  # shutdown py's
        tearDown()

    #################
    #     Logging   #
    #################
    # if reset_initiated == False and in_air_bool == True: # only log packets if the drone is flying
    if True:  # constant logging
        log_pos_bool = True  # call client to get drone kinematics from unity and log
        print_bool = False  # print to console
        add_to_log(log_pos_bool, print_bool, nspTstamp, actions)

    return

# If port and ip are not specified, udp_socket_helper.py should pull from constants.yaml
bgUDPSocket = BGUDPSocket(
    UDPHostName_Address=UDPHostName_Address,
    #bgHomeConfig=bgHomeConfig,
    #debugger=debugger,
    handlePacket=interact,  # Looping control function
    udpRecvPort=udpRecvPort,
    udpSendOnlyPort=udpSendOnlyPort,  # "Send from" port
    rtmUdpHost=rtmUdpHost,  # Send feedback to real time model at this IP
    rtmUdpPort=rtmUdpPort   # ... and at this port
)

bgUDPSocket.initSocket()  # Initializes socket, so it is ready to call recv()

async def start():
    await asyncio.create_task(bgUDPSocket.loop())
    """
    coroutines = [
        asyncio.create_task(bgUDPSocket.loop()),        
        #asyncio.create_task(self.bgWebSocket.receiveLoop()),
        #asyncio.create_task(self.extraLoggers.systemStatsLoggerLoop()),
        #asyncio.create_task(self.extraLoggers.keyboardLoggerLoop()),
        #asyncio.create_task(self.extraLoggers.activityLoggerLoop()),
        #asyncio.create_task(self.checkIfParentProcessIsRunning()),
    ]
    await asyncio.gather(*coroutines)
    """



def add_to_log(log_pos_bool, print_bool, nspTstamp, actions):
        gameTime = time.time() - start_time
        if print_bool == True:
            cur = [nspTstamp, actions[0], actions[1], actions[2]]
            cur = [round(num, 10) for num in cur]
            print(cur)
        # Logging command
        if log_pos_bool == True:
            line = [nspTstamp, actions[0], actions[1], actions[2]]  # : TODO add in-game characteristics to log
            line = [round(num, 10) for num in line]
            send_feedback_to_model(
                nspTimestamp=nspTstamp,
                gameTime=gameTime,
                userInput=actions[:2],  # X,Y
                discreteGesture=actions[2])

        else:
            line = [nspTstamp, actions[0], actions[1], actions[2]]
            line = [round(num, 10) for num in line]
        m = ','+','.join(map(str, line))  # add comma before because each line is prepended with "ROOT:" from debugger
        logging.info(m)  # log locally


def send_feedback_to_model(nspTimestamp, gameTime, userInput, discreteGesture):
    # Set indices
    nspTimestampIdx = 1
    gameTimeIdx = 2
    #PositionXIdx = 3
    #PositionYIdx = 4
    #PositionZIdx = 5
    #userInputXIdx = 6
    #userInputYIdx = 7
    discreteActionIdx = 14
    # Set values
    packetArray = [0.0 for _ in range(64)]
    packetArray[nspTimestampIdx] = float(nspTimestamp)
    packetArray[gameTime] = float(gameTime)
    packetArray[discreteActionIdx] = float(discreteGesture)
    # Send back to model
    bgUDPSocket.send(packetArray)


def tearDown():
    logging.debug("Tearing down")
    bgUDPSocket.stop()              # close UDP socket
    return

if __name__ == '__main__':
    print("Simulation launched...")
    try:
        asyncio.get_event_loop().run_until_complete(start())
    except (KeyboardInterrupt, SystemExit):
        print(" Quitting...")
        logging.debug('Quitting')
        tearDown()
        #raise
        exit()
