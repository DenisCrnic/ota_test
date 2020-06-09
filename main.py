from ota_updater import OTAUpdater
import main

def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/DenisCrnic/ota_test/')
    o.download_and_install_update_if_available('Denis', 'ljubljana')


def start():
    main1 = main.Main()
    # your custom code goes here. Something like this: ...


def boot():
    download_and_install_update_if_available()
    start()

boot()