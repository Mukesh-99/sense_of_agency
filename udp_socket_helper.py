"""
Essentially the same file as:
bg-home/effector_control/ec_lib/udp_socket.py
"""

import asyncio
from datetime import datetime, timezone, timedelta
import struct
from socket import (
    socket,
    timeout as sockettimeoutexception,
    AF_INET,
    SOCK_DGRAM,
    SOL_SOCKET,
    SO_RCVBUF,
    SO_REUSEADDR,
)

import traceback
import os
"""
import yaml
from misc_helpers import getAbsolutePath, getIPAddressFromSubnet


# Getting IP address and port number to receive UDP packets
constantsRelFilePath = os.path.join("src", "constants.yaml")
constantsAbsFilePath = getAbsolutePath(constantsRelFilePath)
with open(constantsAbsFilePath, "r") as f:
    constants = yaml.safe_load(f)

UDP_RECEIVE_PORT = constants["UDP_RECEIVE_PORT"]
CART_SUBNET = constants["CART_SUBNET"]
"""

# Get constraints, or hardcode
""""
from ec_lib.constants import (
    CART_SUBNET,
    UDP_SENDFROM_PORT,
    UDP_RECEIVE_PORT,
    RTM_UDP_PORT,
    SIM_UDP_PORT,
)
from ec_lib.misc_helpers import getIPAddressFromSubnet
from ec_lib.debugger import LogLevel
"""

class BGUDPSocket:
    """Class to handle UDP communication (receive, as well as send) with other BrainGate
    components (Real-Time Model mainly).
    """

    def __init__(
        self,
        handlePacket,
        UDPHostName_Address=None,
        #bgHomeConfig,
        #debugger,
        udpRecvPort=None,
        #udpSendOnlyPort=None,
        bufferSize=1024,
        socketRecvBufferSize=None,
        udpSendOnlyPort=None, # "Send from" port
        rtmUdpHost=None,      # Send feedback to real time model at this IP
        rtmUdpPort=None       # ... and at this port
    ):
        """
        :param dict bgHomeConfig: Config values for running BG Home. Defaults are
            defined in this project, but a user can override them for their device.
        :param debugger.Debugger debugger:
        :param func handlePacket: Function that takes two arguments, udpPacket and game_state.
            Return whatever you want, or nothing. udpPacket is a bytes object. See
            EffectorControl.operateMouse for an example.
        :param int udpRecvPort: (*optional*) Tests that run too close together complain
            about addresses being in use even though sockets get correctly closed. This
            arg allows specifying non-overlapping ports across tests.
        :param int udpSendOnlyPort: (*optional*) Same reason as udpRecvPort but for our
            socket which is used for sending only.
        :param int bufferSize: (*optional*) Maximum number of bytes to be read upon
            receiving a message.
        :param int socketRecvBufferSize: (*optional*) Size of socket's receive buffer.
            Packets that arrive when the socket is not ready (i.e. when it's not mid
            .recv()) are put into the receive buffer, but only up to this many bytes.
            Default is around 2 ** 16 = 65536.
        """  # params descriptions

        #self.bgHomeConfig = bgHomeConfig  # params here
        #self.debugger = debugger
        #self.trace = self.debugger.trace

        self.handlePacket = handlePacket
        # For receiving UDP messages to control the effector.
        self.udpSocket = None
        self.udpHost = UDPHostName_Address #or getIPAddressFromSubnet(CART_SUBNET)
        self.udpPort = udpRecvPort #or UDP_RECEIVE_PORT
        self.bufferSize = bufferSize
        self.socketRecvBufferSize = socketRecvBufferSize

        # Second udp socket for sending only (see docstring of `initSendOnlySocket`).
        self.udpSendOnlySocket = None
        self.udpSendOnlyPort = udpSendOnlyPort
        # Where we send UDP messages to.
        self.rtmUdpHost = rtmUdpHost #self.bgHomeConfig["Network"]["RTM_UDP_HOSTNAME"]
        self.rtmUdpPort = rtmUdpPort #RTM_UDP_PORT

        """
        ## Error handling during msg handling.
        self.recentMsgHandlingErrors = {}
        self.errorLogMilestones = [1, 2, 3, 4, 5, 10, 100, 1000]
        self.errorLogTimeout = timedelta(seconds=30)
        """
        # Allow ending the receive loop.
        self.isStopped = False

    async def loop(self, game_state):
        """Loop and receive UDP packets at the specified address (host and port). While
        the receiving socket is closed, just pass.
        """
        # Not sending back (for now)
        await self.runWithRetry(self.initSendOnlySocket, "Init send-only socket failed")

        while not self.isStopped:
            # If socket is closed, wait before trying again.
            if not self.isSocketReady():
                await asyncio.sleep(0.1)
                continue
            try:
                udpPacket = self.udpSocket.recv(self.bufferSize)
            except sockettimeoutexception:
                # Our socket's timeout is basically 0, so this happens plenty and it's
                # fine.
                pass
            except Exception as e:
                """
                self.trace(f"Receive failed: {e}", logLevel=LogLevel.WARN)
                """
                print("self.trace(Receive failed: {}, logLevel=LogLevel.WARN)".format(str(e)))
                pass  # not error handling for now
            else:
                if udpPacket:
                    try:
                        self.handlePacket(udpPacket, game_state)  # Success! Interpret the message
                    except Exception as e:
                        #self.logMsgHandlingError(e)
                        print("self.logMsgHandlingError( {} )".format(str(e)))
                        pass

            # Relinquish control so other asyncio loops can progress.
            await asyncio.sleep(0.001)

    def stop(self):
        """End the loop in .loop() and perform tear down (closing the socket)."""
        self.isStopped = True
        self.closeSocket()
        self.closeSendOnlySocket()

    def initSocket(self):
        """Create and bind the socket object for receiving UDP. After this, it's ready
        to call .recv().
        """
        # Check if already ready to go.
        if self.isSocketReady():
            return

        self.udpSocket = socket(AF_INET, SOCK_DGRAM)
        # Socket Options
        self.udpSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
        # (non-None timeout so recv doesn't block)
        # (non-0 timeout so recv doesn't error when it got no data)
        self.udpSocket.settimeout(0.001)

        if self.socketRecvBufferSize is not None:
            self.udpSocket.setsockopt(SOL_SOCKET, SO_RCVBUF, self.socketRecvBufferSize)

        # Bind socket
        self.udpSocket.bind((self.udpHost, self.udpPort))
        #self.trace(f"UDP socket bound to host: {self.udpHost}, port: {self.udpPort}.")
        print("UDP socket bound to host:",self.udpHost,", port:",self.udpPort,".")

    def closeSocket(self):
        """Close the socket object.

        Called in this class's .stop() method, but can also be called without stopping
        the loop. To continue receiving commands again, call .initSocket() again to
        create another socket.
        """
        if self.isSocketReady():
            self.udpSocket.close()

    def send(self, packetArray):
        #Send a UDP message to the RTM
        #:param float[] packetArray: Array of data to send. Will be converted to the
        #    bytes representation of an array of doubles.
       
        if not self.isSendOnlySocketReady():
            return

        # Create the packet to send.
        packetBytes = b"".join(struct.pack("d", field) for field in packetArray)
        # Send to RTM.
        try:
            self.udpSendOnlySocket.sendto(
                packetBytes, (self.rtmUdpHost, self.rtmUdpPort)
            )
        except OSError as e:
            errMsg = f"Error sending feedback to model: {e}"
            print(errMsg)

    ####################################################################################
    #
    #   Helpers
    #
    ####################################################################################
    def isSocketReady(self):
        """Return boolean for if the socket object exists and is open for receiving."""
        return self.udpSocket is not None and self.udpSocket.fileno() != -1

    def isSendOnlySocketReady(self):
        #Return boolean for if our send-only socket object exists and is open for
        #sending.
        return (
            self.udpSendOnlySocket is not None and self.udpSendOnlySocket.fileno() != -1
        )

    def initSendOnlySocket(self):
        #We use a second socket/port for sending only because on Windows if a UDP msg
        #fails to be delivered, an ICMP msg (10054) is returned to the sending socket and
        #is difficult for us to handle gracefully (we should be only receiving RTM command
        #packets so it unnecessarily complicates our receiving logic, and also our socket
        #stops receiving altogether after some seconds). In production this doesn't
        #happen because our sends generally succeed, but in development we may have no
        #RTM receiving EC's feedback msgs, so they all fail to deliver, resulting in this
        #issue.
        #While the regular UDP socket is expected to be closed and opened (to share the
        #port with other programs on this device that listen for RTM commands), this
        #send-only socket should stay open until it is closed at the end of the process.
        self.udpSendOnlySocket = socket(AF_INET, SOCK_DGRAM)
        # Bind socket
        self.udpSendOnlySocket.bind((self.udpHost, self.udpSendOnlyPort))
        print("SendOnly socket:",self.udpHost,", port:",self.udpSendOnlyPort,".")
        #self.trace(
        #    f"UDP send-only socket bound to host: "
        #    + f"{self.udpHost}, port: {self.udpSendOnlyPort}."
        #)

    def closeSendOnlySocket(self):
        #Close our send-only socket object.
        if self.isSendOnlySocketReady():
            self.udpSendOnlySocket.close()

    """
    def logMsgHandlingError(self, exception):
        #Log an error that occurred while handling a received packet. In case we get
        #a ton rapidly, to avoid creating a giant log file, check for repeat error
        #messages and only log some.
        #:param Exception|string exception:
        
        now = datetime.now(tz=timezone.utc)
        errMsg = f"Error while handling UDP packet: {traceback.format_exc()}"
        # If haven't seen this error before, initialize a dict for it.
        if errMsg not in self.recentMsgHandlingErrors:
            self.recentMsgHandlingErrors[errMsg] = {
                "count": 0,
                "lastLoggedTime": now,
            }
        errRecencyDict = self.recentMsgHandlingErrors[errMsg]
        # If it's been long enough since logging this error, reset this error's count.
        if now - errRecencyDict["lastLoggedTime"] > self.errorLogTimeout:
            errRecencyDict["count"] = 0
        # Increment this error's count.
        errRecencyDict["count"] += 1
        # If we're at a milestone number of this error, log it.
        if errRecencyDict["count"] in self.errorLogMilestones:
            self.trace(
                f"({errRecencyDict['count']}) {errMsg}",
                logLevel=LogLevel.ERROR,
                alertHuman=True,
            )
            errRecencyDict["lastLoggedTime"] = now
    """  # Error logging

    async def runWithRetry(self, func, logMsg, interval_sec=5, maxAlerts=5):
        """Run some code until it succeeds, and log each time it errors.

        :param () -> None func: Code to run, no arguments or return value.
        :param string logMsg: Msg to log to our log file with the error if this code
            fails.
        :param float interval_sec: How many seconds after failing before retrying.
        :param int maxAlerts: How many times to error before we stop alerting about it.
        """
        numTimesErrored = 0

        while True:
            try:
                func()
                break
            except Exception as e:
                print("error in runWithRetry")
                numTimesErrored += 1
                #errMsg = f"{logMsg}: {e}"
                doAlert = numTimesErrored <= maxAlerts
                #self.trace(errMsg, logLevel=LogLevel.ERROR, alertHuman=doAlert)
                if numTimesErrored == maxAlerts:
                    lastAlertMsg = (
                        f'Alerted about "{logMsg}" {maxAlerts} times. '
                        "Will continue retrying, but stop alerting about it."
                    )
                    #self.trace(lastAlertMsg, logLevel=LogLevel.WARN, alertHuman=doAlert)
                    print("numTimesErrored == maxAlerts")
                await asyncio.sleep(interval_sec)