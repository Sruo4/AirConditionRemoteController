import utime
import ujson
import gc


import network


def connectWIFI():
    print('Connecting wifi...')
    sta_wlan = network.WLAN(network.STA_IF)
    sta_wlan.active(True)
    sta_wlan.connect('Fhe14', '18042475359', security=network.AUTH_PSK)
    while(sta_wlan.config() == '0.0.0.0'):
        utime.sleep(1)
    print('Connected...')

connectWIFI()
