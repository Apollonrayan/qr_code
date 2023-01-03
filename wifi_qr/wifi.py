import segno
from segno import helpers
import os

qrcode = helpers.make_wifi(ssid='Campus Condorcet Colloques', password='Campus93!', security='WPA')
qrcode.designator
'3-M'
qrcode.save('wifi-access.png', scale=10)

