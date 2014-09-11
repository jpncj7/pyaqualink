##################################################################
# configuration
##################################################################
logFileName = "aqualink.log"

debug = True                        # general debug messages
debugData = False                   # show parsed aqualink messages
debugRaw = False                    # show all raw RS485 data
debugAck = False                     # show ack messages
debugStatus = False                  # show status messages received from controller
debugAction = False                  # show action messages sent to to controller
debugMsg = True                    # show text messages received from controller
debugHttp = False
debugWeb = False

RS485Device = "/dev/ttyUSB0"        # RS485 serial device to be used
RS232Device = "/dev/stdin"          # RS232 serial device to be used
allButtonPanelAddr = '\x09'         # address of All Button control panel
httpPort = 80                       # web server port
monitorMode = False                 # true if monitoring another panel

