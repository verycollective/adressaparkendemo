Python example for interacting with adressaparken

# Setup
- Install python 3 https://www.python.org/downloads/
- Run `pip3 install bottle soundfile numpy sounddevice` to install requirements for example code
- Start server with `python3 server.py`

By default is the MOTU soundcard (192.168.2.21) is connected to MAC1 by USB and is the easiest computer to play sound from. If you want to connect your own computer to the MOTU soundcard you need to install MOTU Pro Audio Installer http://motu.com/download (drivers for interacting with the sound card through AVB)

Sound lib docs: http://python-sounddevice.readthedocs.io/en/0.3.10/index.html

Tool for using your server outside the local network: https://localtunnel.github.io/www/
