import argparse, socket, time
import imp, signal, sys

from artnet import buildPacket
from matrix import *

try:
    from MatrixSim.MatrixScreen import *
except Exception, e:
    print e
UDP_PORT = 6454

parser = argparse.ArgumentParser()
parser.add_argument("--fps",        help="control flow speed. if 0 fps is fastest possible.",   metavar="<fps>",            nargs="?", default=15,                  type=float)
parser.add_argument("--config",     help="load config.",                                        metavar="<config_conf.py>", nargs="?", default="default_conf.py",   type=str)
parser.add_argument("--snakeMode",  help="flips every x amount of data",                        metavar="<enabled>",        nargs="?", default=None,                type=str)
parser.add_argument("--matrixSim",  help="turns on buildin matrix simulation",                  metavar="<enabled>",        nargs="?", default=None,                type=str)
parser.add_argument("--pixelSize",  help="sets the pixel size for the matrix sim",              metavar="<size>",           nargs="?", default=30,                  type=int)
parser.add_argument("--netSilent",  help="if enabled won't send out udp packets anywhere",      metavar="<enabled>",        nargs="?", default=None,                type=str)
parser.add_argument("--showFps",    help="prints out the actuall fps the program runs at",      metavar="<enabled>",        nargs="?", default=None,                type=str)
parser.add_argument("--fullscreen", help="makes matrixsim go fullscreen (hides mouse pointer)", metavar="<enabled>",        nargs="?", default=False,               type=str)
#parser.add_argument("--matrixSize", help="set the width and hight of matrix for exampel: --matrixSize=10,17", nargs="+", type=int)
args = parser.parse_args()

#the bit below here allows loading of the config files specified by --config written by Duality
#this will then also load patterns.
package = "configs"
fp, path, description = imp.find_module(package)
fp, path, description = imp.find_module(str(args.config)[:-3], [path])
config = imp.load_module("configuration", fp, path, description)
TARGETS = config.TARGETS
#---------

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(False)

def signal_handler(signal, frame):
    print "\nExiting closing connections."
    sock.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

#setup a screen if matrixSim argument was set.
if args.matrixSim == "enabled":
    if args.fullscreen == "enabled":
        fullscreen=True
    else:
        fullscreen=False
    matrixscreen = MatrixScreen(matrix_width, matrix_height, args.pixelSize, fullscreen)

if args.fps > 0:
    fps = 1./args.fps

#sendout function that sends out data to the networked devices and
#also to the matrix screen simulator if enabled.
#or only to the matrix simulator if netSilent enabled.
def sendout():
    for t in TARGETS:
        pattern = TARGETS[t]
        data = pattern.generate()
        #convert the data for the special matrix layout.
        if args.snakeMode == "enabled":
            data = convertSnakeModes(data)
        #if this is a simulation draw it to the matrixscreen else 
        #send it out over the network.
        if not (args.netSilent == "enabled"):
            sock.sendto(buildPacket(0, data), (t, UDP_PORT))
        #make sure matrixSim always displays the data the right way.
        if args.matrixSim == "enabled":
            try:
                if args.snakeMode == "enabled":
                    matrixscreen.process(convertSnakeModes(data))
                else:
                    matrixscreen.process(data)
            #matrix sim needs this because i am to lazy to press the x button.
            except KeyboardInterrupt:
                signal_handler(None, None)

#hold values for time.
current = 0
previous = 0

while(True):
    #send patterns out in a timed fasion. if args.fps != 0
    if args.fps > 0:
        current = time.time()
        if (current-previous) >= fps:
            previous = time.time()
            sendout()
    #else send everything out as fast as possible
    else:
        sendout()
signal_handler(None, None)
