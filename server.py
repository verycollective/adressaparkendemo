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

@route('/light/<address>')
def light(address):
    artnet_subnet = 0
    artnet_net = 0
    artnet_universe = 0
    ip = '192.168.1.10'
    port = 6454
    address = int(address) # 1 - 11 - 21 - 31- 41 - 51 - 61 - 71 - 81 - 91
    value = randint(0, 255)

    device = ArtNet_send.ArtNet_send(artnet_net, artnet_subnet, artnet_universe, ip, port)
    device.send_single_value(address, value)
    return "OK"

@route('/video')
def video():
    #todo show small video clip with hippo server
    return "OK"

run(host='0.0.0.0', port=8080)