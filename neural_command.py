"""
File from:

bg-home/effector_control/ec_lib/neural_command.py

"""

import struct
import numpy as np

class NeuralCommand(object):
    """Class to hold the logic for parsing a neural command udp message from the
    Real-Time Model in Simulink
    """

    packetIDIdx = 0
    nspTimestampIdx = 1
    xIdx = 2
    yIdx = 3
    discreteActionIdx = 4
    commandCounterIdx = -1

    def __init__(self, packetID, nspTimestamp, x, y, discreteAction, commandCounter=0):
        self.packetID = packetID
        self.nspTimestamp = nspTimestamp
        self.x = x
        self.y = y
        self.discreteAction = discreteAction
        self.commandCounter = commandCounter

    @classmethod
    def fromBytes(cls, msgBytes):
        ###print("ENTERED", msgBytes)
        """Way to initialize an instance of NeuralCommand from raw bytes, for example
            as might be sent from the real-time model via UDP.

        :param bytes msgBytes: message bytes constructed the way the real-time model
            constructs neural command packets, with x, y, etc. in particular indices of
            the packet
        """
        msgDoubles = np.frombuffer(msgBytes, dtype=np.double)
        ###print("msgDoubles", msgDoubles)
        packetID = float(msgDoubles[cls.packetIDIdx])
        nspTimestamp = float(msgDoubles[cls.nspTimestampIdx])
        x = float(msgDoubles[cls.xIdx])
        y = float(msgDoubles[cls.yIdx])
        discreteAction = float(msgDoubles[cls.discreteActionIdx])
        commandCounter = int(msgDoubles[cls.commandCounterIdx])
        ###print("RET", packetID, nspTimestamp, x, y, discreteAction,commandCounter)
        return cls(
            packetID, nspTimestamp, x, y, discreteAction, commandCounter=commandCounter
        )

    def toPacketBytes(self):
        """The opposite direction of fromBytes.

            Used for testing. The real packet bytes generation happens in the real-time
            model in Simulink.

        :returns bytes packet: the bytes should follow the structure that the Real-Time
            Model in Simulink uses when sending these command packets out
        """
        msgBytes = b"".join(
            struct.pack("d", field)
            for field in [
                self.packetID,
                self.nspTimestamp,
                self.x,
                self.y,
                self.discreteAction,
                self.commandCounter,
            ]
        )
        return msgBytes