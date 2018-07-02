# This code belongs to by Leon R, license unknown
# https://github.com/itsLeonR/python-artnet


import socket
import struct
import sys

class ArtNet_send(): # Class to make an Artnet-Packet
    packet_counter = 1
    dmxdata = [0, 0]

    def __init__(self, artnet_net, artnet_subnet, artnet_universe, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.net = int(artnet_net)
        self.subnet = int(artnet_subnet)
        self.universe = int(artnet_universe)
        self.ip = ip
        self.port = int(port)

    def send_single_value(self, adr, value):
        if adr < 1 or adr > 512:
            return

        while len(self.dmxdata) < adr:
            self.dmxdata.append(0)
        self.dmxdata[adr - 1] = value
        self.make_packet()

    def make_packet(self):
        data = []
        data.append("Art-Net\x00")
        data.append(struct.pack('<H', 0x5000))
        data.append(struct.pack('>H', 14))
        data.append(struct.pack('B', self.packet_counter))
        self.packet_counter += 1
        if self.packet_counter > 255:
            self.packet_counter = 1
        data.append(struct.pack('B', 0))
        data.append(
            struct.pack('<H', self.net << 8 | self.subnet << 4 | self.universe))
        data.append(struct.pack('>H', len(self.dmxdata)))
        for d in self.dmxdata:
            data.append(struct.pack('B', d))
        result = bytes()
        for token in data:
            try:  # Handels all strings
                result = result + token.encode('utf-8', 'ignore')
            except:  # Handels all bytes
                result = result + token

        self.s.sendto(result, (self.ip, self.port))

    def close(self):
        self.s.close()
