#import all patterns availble for use.
from patterns.Patterns import *

local_host = "localhost"

TARGETS = {
    # local_host:BarberpolePattern(),
     # local_host:OldTron(),
      #local_host:Tron(),
    # local_host:Snake(speed=17),
    
    # MixedLife() doesn't work atm but will be fixed
    # local_host:MixedLife(),
#     local_host:RandomLife(),
 #    local_host:BlueLife(),
    # raspberrypi:BlueLife(),
    local_host:sven(),	 
    # local_host:SuperPixelBros(),
#     local_host:Pong(speed=5),
    # pixelMatrix:Pong(speed=3),
    # pixelMatrix:Pong(speed=8),
    # pixelMatrix:Snake(),
    # local_host:BlueLife(),

    # #needs images. wip still.
    # local_host:DisplayPng(),

    # local_host:PlasmaFirst(),
#     local_host:PlasmaSecond(),
    # michiel_laptop:PlasmaSecond(),
    # local_host:PlasmaThird(),
    
#    local_host:RainPattern(chance=0.2),
    
     #local_host:GraphicsCircleTest(),
    # local_host:GraphicsRectTest(),
#    local_host:GraphicsLineTest(),
     #local_host:GraphicsPixelTest(),
    # local_host:GraphicsDotTest(),
}
