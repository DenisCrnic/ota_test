from main import ota_updater

import network

ssid = 'Denis'
password = 'ljubljana'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

def hello():
  print("HELLO WORLD 2.4")