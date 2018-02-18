Demo python example for interacting with adressaparken

# Setup
- Install MOTU Pro Audio Installer http://motu.com/download (drivers for interacting with the sound card through AVB)
- Setup connection from computer to MOTU soundcard http://motu.com/avb/using-your-motu-avb-device-as-a-mac-audio-interface-over-avb-ethernet/
- Install python 3 https://www.python.org/downloads/
- Run `pip3 install bottle soundfile numpy` to install requirements for example code
- Install sounddevice http://python-sounddevice.readthedocs.io/en/0.3.10/index.html (to be able to route sound to desired sound device with python)
- Start server with `python3 server.py`



By default the MOTU soundcard (192.168.2.21) is connected to MAC1 and is the easiest way to play sound.
http://motu.com/techsupport/technotes/microbook-ii-routing-one-or-more-sources-to-multiple-outputs

To use more then two channels http://motu.com/techsupport/technotes/microbook-ii-routing-one-or-more-sources-to-multiple-outputs




Enable AVB on switch https://www.extremenetworks.com/wp-content/uploads/2014/10/Using-AVB-with-Extreme-Switches.pdf