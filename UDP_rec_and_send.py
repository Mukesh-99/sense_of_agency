"""
UDP_rec_and_send.py
Receives UDP packets from a socket (from RTM) and sends logs back to the RTM
Author: Derek Wacks

Class to handle UDP communication between the BrainGate Real-Time Model
and research session experiments built in Python.

Facilitate UDP packet receiving and game state logging (sending back to RTM)

"""

print("\n\nIN UDP_rec_and_send!\n\n")


# Imports
import time
import sys
import math
import numpy as np
from udp_socket_helper import BGUDPSocket
from neural_command import NeuralCommand
import asyncio
import logging


####################
# Initial log file #
####################
logging_locally = False
if logging_locally:
    curr_t = time.asctime().replace(" ", "_").replace(":", "_")
    log_dir_loc = '../../Data/GameData/CURRENTLOG/'
    fname = log_dir_loc + curr_t + '_exp_0.log'  # writes to Data/ (outside of research-sessions)
    logging.basicConfig(filename=fname, level=logging.DEBUG)
    header = "UPDATE HEADERS HERE"  # adding header to view log file as csv
    logging.info(header)

###############
# IP and port #
###############
# Test settings for locally sending commands as packets
testing_bool = False  # CHANGE BEFORE SESSION (COFFEE)
if testing_bool:
    udpRecvPort = 26504  # originally testing on 8667
    UDPHostName_Address = "192.168.30.3"  # PC2 (staticly set)
    #UDPHostName_Address = "192.168.30.1"  # PC1 (staticly set)
    #loc = "192.168.30.1" # Python scripts running on PC1 # NOT USING
    #UDPHostName_Address = "127.0.0.1"
else:
    udpRecvPort = 26504
    UDPHostName_Address = "192.168.30.100"  # T11 personal comp staticly set FOR R_SESSION
    #loc = "192.168.30.3" # Python scripts running on PC2 # NOT USING

############################
# IP/port for RTM feedback #
############################
udpSendOnlyPort = 26400  # "Send from" port
rtmUdpPort = 26400  # Send feedback to real time model at this IP
rtmUdpHost = "192.168.30.4"


#############
#   Params  #
#############
#start_time = time.time()  # in-game start time

def logging_fn(udpPacket, game_state):
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
    input = [x, y, discrete_click]
    send_feedback_to_model(nspTstamp, game_state, input)
    return

# If port and ip are not specified, udp_socket_helper.py should pull from constants.yaml
bgUDPSocket = BGUDPSocket(
    UDPHostName_Address=UDPHostName_Address,
    #bgHomeConfig=bgHomeConfig,
    #debugger=debugger,
    handlePacket=logging_fn,  # Looping logging function
    udpRecvPort=udpRecvPort,
    udpSendOnlyPort=udpSendOnlyPort,  # "Send from" port
    rtmUdpHost=rtmUdpHost,  # Send feedback to real time model at this IP
    rtmUdpPort=rtmUdpPort   # ... and at this port
)

bgUDPSocket.initSocket()  # Initializes socket, so it is ready to call recv()

async def start(game_state):
    await asyncio.create_task(bgUDPSocket.loop(game_state))
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


# NOT USING
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

def send_feedback_to_model(nspTimestamp, game_state, userInput, gameTime=None):
    # Set indices
    nspTimestampIdx = 1
    gameTimeIdx = 2
    #PositionXIdx = 3
    #PositionYIdx = 4
    #PositionZIdx = 5
    discreteActionIdx = 14
    # PUT GAMESTATE DATA HERE
    game_data1_Idx = 37
    game_data2_Idx = 38

    # Set values
    x, y, discreteGesture = userInput
    game_state["time_entered_state"] = time.time()
    curr_state = game_state["current_state"]
    game_time_when_entered = game_state["time_entered_state"]

    packetArray = [0.0 for _ in range(64)]
    packetArray[nspTimestampIdx] = float(nspTimestamp)
    if gameTime:
        packetArray[gameTime] = float(gameTime)
    packetArray[discreteActionIdx] = float(discreteGesture)
    # Send back to model
    packetArray[game_data1_Idx] = float(curr_state)
    packetArray[game_data2_Idx] = float(game_time_when_entered)

    bgUDPSocket.send(packetArray)

def tearDown():
    logging.debug("Tearing down")
    bgUDPSocket.stop()              # close UDP socket
    return

def start_loop(game_state):
    print("Experiment launched...")
    try:
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)#.run_until_complete(start(game_state))
        asyncio.get_event_loop().run_until_complete(start(game_state)) # instead of 2 lines above
    except (KeyboardInterrupt, SystemExit):
        print(" Quitting...")
        logging.debug('Quitting')
        tearDown()
        exit()