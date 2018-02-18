from bottle import route, run, template
import sounddevice as sd
import soundfile as sf
from lib import ArtNet_send
from random import randint

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
    #todo mapping with hexagonal speaker setup on MAC1
    speaker = int(speaker)
    sd.play(mono, fs, mapping=[speaker])
    return "OK"

@route('/lightrandom/<address>')
def lightrandom(address):
    return lightsingle(address, randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))

@route('/lightallblue')
def allblue():
    lightsingle(1, 0, 0, 50, 5)
    lightsingle(11, 0, 0, 50, 5)
    lightsingle(21, 0, 0, 50, 5)
    lightsingle(31, 0, 0, 50, 5)
    lightsingle(41, 0, 0, 50, 5)
    lightsingle(51, 0, 0, 50, 5)
    lightsingle(61, 0, 0, 50, 5)
    lightsingle(71, 0, 0, 50, 5)
    lightsingle(81, 0, 0, 50, 5)
    lightsingle(91, 0, 0, 50, 5)
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

@route('/lightsingle/<address>/<r>/<g>/<b>/<w>')
def lightsingle(address, r, g, b, w):
    artnet_subnet = 0
    artnet_net = 0
    artnet_universe = 0
    ip = '192.168.1.10'
    port = 6454
    address = int(address) # 1 - 11 - 21 - 31- 41 - 51 - 61 - 71 - 81 - 91
    device = ArtNet_send.ArtNet_send(artnet_net, artnet_subnet, artnet_universe, ip, port)
    device.send_single_value(address, r)
    device.send_single_value(address+1, g)
    device.send_single_value(address+2, b) 
    device.send_single_value(address+3, w)
    return "OK"

@route('/video')
def video():
    #todo show small video clip with hippo server
    return "OK"

run(host='0.0.0.0', port=8080)