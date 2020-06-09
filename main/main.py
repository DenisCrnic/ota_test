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

def download_and_install_update_if_available():
  o = OTAUpdater('https://github.com/DenisCrnic/ota_test')

  o.download_and_install_update_if_available('Denis', 'ljubljana')
  o.check_for_update_to_install_during_next_reboot()


def start():
  print("Hello world! 1.8")
  pass
    # your custom code goes here. Something like this: ...
    # from main.x import YourProject
    # project = YourProject()
    # ...

def boot():
  download_and_install_update_if_available()
  start()

boot()