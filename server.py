from bottle import route, run, template
import sounddevice as sd
import soundfile as sf
from random import randint
from lib.StupidArtnet import StupidArtnet


@route('/')
def menu():
	"""Build html interface."""
	return template('menu')


@route('/sound/<speaker>')
def sound(speaker):
	"""Play demo sound in speaker."""
	data, fs = sf.read('bell.wav', dtype='float32')

	# To see available sound devices, use python3 -m sounddevice
	sd.default.device = '24Ao'
	# sd.default.device = 'Built-in Output' # OS x default

	mono = [(sample[0] + sample[1]) / 2 for sample in data]  # convert to mono

	speaker = int(speaker)
	sd.play(mono, fs, mapping=[speaker], blocking=False)  # remove mapping to test without soundcard
	return "OK"


@route('/lightrandom/<address>')
def lightrandom(address):
	"""Set light to random colour."""
	return lightsingle(address, randint(0, 255), randint(0, 255), randint(0, 255))


@route('/lightall/<sr>/<sg>/<sb>')
def allblue(sr, sg, sb):
	"""Set all lights to blue."""
	global a
	r = int(sr)
	g = int(sg)
	b = int(sb)
	for ad in dmx_adresses:
		a.set_rgb(ad, r, g, b)
	return "OK"


@route('/lightallrandom')
def allrandom():
	"""Set all lights to random colours."""
	global a
	for ad in dmx_adresses:
		a.set_rgb(ad, randint(0, 255), randint(0, 255), randint(0, 255))
	return "OK"


@route('/blackout')
def blackout():
	"""Set all lights off."""
	global a
	a.blackout()
	return "OK"


@route('/lightsingle/<address>/<r>/<g>/<b>')
def lightsingle(address, r, g, b):
	"""Set given RGB values to light."""
	global a
	address = int(address)  # 1 - 4 - 7 - 10 - 13 - 16 - 19 - 22 - 25 - 28

	# SET THE ARTNET BUFFER TO OUR DATA ...
	a.set_rgb(address, r, g, b)
	return "OK"


@route('/video')
def video():
	"""NYI."""
	# todo show small video clip with hippo server
	return "OK"


# Addresses for the LEDs as installed
dmx_adresses = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]

# VALUES SET FOR THE ADRESSAPARKEN FIXED INSTALL
target_ip = '192.168.1.185'  # typically in 2.x or 10.x range
packet_size = 32             # it is not necessary to send whole universe
universe = 0

# CREATING A STUPID ARTNET OBJECT
# TARGET_IP   = DEFAULT 127.0.0.1
# UNIVERSE    = DEFAULT 0
# PACKET_SIZE = DEFAULT 512
# FRAME_RATE  = DEFAULT 30
a = StupidArtnet(target_ip, universe, packet_size)

# SEE IF EVERYTHING IS OK
print(a)

# START ARTNET THREAD
a.start()

try:
	run(host='0.0.0.0', port=8080)
finally:
	print("Quitting")
	del a
