from ota_updater import OTAUpdater


def download_and_install_update_if_available():
  o = OTAUpdater('https://github.com/DenisCrnic/ota_test')
  o.download_and_install_update_if_available('Denis', 'ljubljana')


def start():
  print("Hello world!")
  pass
    # your custom code goes here. Something like this: ...
    # from main.x import YourProject
    # project = YourProject()
    # ...

def boot():
  download_and_install_update_if_available()
  start()


boot()