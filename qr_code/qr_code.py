import pyqrcode
import png
url = pyqrcode.create('http://www.twitter.com/vlevinski')
#url.png('vlevinski.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
url.png('vlevinski.png', scale=6)
