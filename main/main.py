from ota_updater import OTAUpdater

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
o = OTAUpdater('https://github.com/DenisCrnic/ota_test')
o.check_for_update_to_install_during_next_reboot()

class Main:

  def __init__(self):
    print("HELLO WORLD 2.0")