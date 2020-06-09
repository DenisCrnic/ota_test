from main import ota_updater

import network

# WiFi Credentials
ssid = 'Denis'
password = 'ljubljana'

# Connection to WiFi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
  pass
print('Connection successful')
print(station.ifconfig())

class Main:
  def __init__(self):
    print("HALLO WORLD 3.3")
    # self.hello()

  # def hello(self):
  #   print("HELLO WORLD 2.10")