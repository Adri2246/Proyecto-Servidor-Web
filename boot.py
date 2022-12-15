import socket

import network
import esp
import gc

esp.osdebug(None)
gc.collect()

ssid = 'Marquito'
password = '1029vazvel'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print("Connection Successful")
print(station.ifconfig())