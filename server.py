from bottle import route, run, template
import sounddevice as sd
import soundfile as sf
from lib import ArtNet_send
from random import randint
from lib.StupidArtnet import StupidArtnet

@route('/')
def menu():
    return template('menu')

@route('/sound/<speaker>')
def sound(speaker):
    data, fs = sf.read('bell.wav', dtype='float32')

    # To see available sound devices, use python3 -m sounddevice
    sd.default.device = '24Ao'
    #sd.default.device = 'Built-in Output' # OS x default

    mono = [(sample[0]+sample[1])/2 for sample in data]; #convert to mono

    speaker = int(speaker)
    sd.play(mono, fs, mapping=[speaker], blocking=False) # remove mapping argument to test on machines without fancy soundcard
    return "OK"

@route('/lightrandom/<address>')
def lightrandom(address):
    return lightsingle(address, randint(0, 255), randint(0, 255), randint(0, 255))

@route('/lightall/<sr>/<sg>/<sb>')
def allblue(sr, sg, sb):
    r = int(sr)
    g = int(sg)
    b = int(sb)
    lightsingle(1, r, g, b)
    lightsingle(11, r, g, b)
    lightsingle(21, r, g, b)
    lightsingle(31, r, g, b)
    lightsingle(41, r, g, b)
    lightsingle(51, r, g, b)
    lightsingle(61, r, g, b)
    lightsingle(71, r, g, b)
    lightsingle(81, r, g, b)
    lightsingle(91, r, g, b)
    return "OK"

@route('/lightallrandom')
def allrandom():
    lightrandom(1)
    lightrandom(11)
    lightrandom(21)
    lightrandom(31)
    lightrandom(41)
    lightrandom(51)
    lightrandom(61)
    lightrandom(71)
    lightrandom(81)
    lightrandom(91)
    return "OK"

@route('/lightsingle/<address>/<r>/<g>/<b>')
def lightsingle(address, r, g, b):
    address = int(address) # 1 - 11 - 21 - 31- 41 - 51 - 61 - 71 - 81 - 91

    # THESE ARE MOST LIKELY THE VALUES YOU WILL BE NEEDING
 #   target_ip = '127.0.0.1'
    target_ip = '192.168.1.4'     # localhost for testing, typically in 2.x or 10.x range
    universe = 0                # see docs
    packet_size = 512           # it is not necessary to send whole universe

    # CREATING A STUPID ARTNET OBJECT
    a = StupidArtnet()

    # SETUP NEEDS FEW SKIPPABLE ELEMENTS
    # TARGET_IP   = DEFAULT 127.0.0.1
    # UNIVERSE    = DEFAULT 0
    # PACKET_SIZE = DEFAULT 512
    a.setup(target_ip, universe)

    # SET THE ARTNET BUFFER TO OUR DATA ...
    a.set_rgb(address, r, g, b)

    # ... AND SEND
    a.show()
    a.show()
    a.show()

    return "OK"

@route('/video')
def video():
    #todo show small video clip with hippo server
    return "OK"

run(host='0.0.0.0', port=8080)
